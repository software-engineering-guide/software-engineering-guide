# 6.2 Rekayasa pembelajaran mesin (MLOps)

## Tinjauan dan motivasi

Rekayasa pembelajaran mesin, biasa disebut [MLOps](https://en.wikipedia.org/wiki/MLOps), adalah disiplin membawa [pembelajaran mesin](https://en.wikipedia.org/wiki/Machine_learning) keluar dari notebook dan eksperimen menuju sistem produksi yang andal, dapat diamati, dan dapat dipelihara. Perangkat lunak tradisional berperilaku sebagaimana dikatakan kodenya. Sistem ML berperilaku sebagaimana dikatakan bersama oleh kodenya, datanya, dan parameter modelnya yang dipelajari. Itu membuat sistem ML lebih sulit diuji, lebih sulit direproduksi, dan rentan gagal secara diam-diam ketika dunia menyimpang dari data tempat ia dilatih. MLOps membawa ketelitian rekayasa perangkat lunak (kontrol versi, pengujian, pengiriman berkelanjutan, dan pemantauan) ke kenyataan tiga bagian ini: kode ditambah data ditambah model.

Bagi tim besar, MLOps adalah pembeda antara model sekali jalan yang memukau dalam demo dan armada model yang dapat dibangun, di-deploy, dan dioperasikan dengan aman oleh banyak tim. Tanpa platform dan praktik bersama, setiap tim menciptakan ulang pipeline data, loop pelatihan, dan deployment, dan Anda berakhir dengan sistem rapuh yang tak dapat direproduksi siapa pun enam bulan kemudian. Enterprise mengandalkan MLOps untuk berskala di puluhan model, memenuhi service-level objective, dan memuaskan auditor yang bertanya bagaimana prediksi tertentu dihasilkan.

Di pemerintah dan industri teregulasi, MLOps sering menjadi persyaratan kepatuhan yang menyamar. Reprodusibilitas, silsilah, dan versioning memungkinkan lembaga menjawab pertanyaan signifikan secara hukum: persisnya model mana, dilatih pada data mana, dengan kode mana, yang menghasilkan keputusan yang memengaruhi seorang warga? Praktik MLOps yang matang menjaga pertanyaan itu dapat dijawab bertahun-tahun kemudian, yang merupakan rekayasa baik sekaligus pengaman hukum.

*Lihat juga:* bab 8.1 (CI/CD dan pengiriman), bab 9.2 (observabilitas dan pemantauan), dan bab 6.6 (infrastruktur dan operasi AI).

## Prinsip utama

- Perlakukan data, kode, dan model sebagai artefak yang diversikan bersama; mengubah salah satunya mengubah perilaku sistem.
- Otomatiskan jalur dari data ke model terlatih ke deployment agar dapat diulang dan diaudit.
- Buat setiap model dapat ditelusuri ke data, kode, dan konfigurasi persis yang menghasilkannya.
- Evaluasi model terhadap data uji representatif sebelum deployment, dan terus evaluasi sesudahnya.
- Asumsikan model memburuk; pantau drift (divergensi bertahap data langsung atau hubungan masukan-keluaran dari apa yang dilatihkan pada model), masalah kualitas data, dan penurunan kinerja sejak hari pertama.
- Pilih pipeline membosankan yang dapat direproduksi daripada eksperimen cerdas yang tak dapat direproduksi.
- Pisahkan perhatian kecepatan eksperimen dan keandalan produksi, dan jembatani keduanya dengan sengaja.

## Rekomendasi

### Kelola siklus hidup ML penuh secara eksplisit

Definisikan dan instrumentasi setiap tahap: ingesti dan validasi data, [rekayasa fitur](https://en.wikipedia.org/wiki/Feature_engineering), pelatihan, evaluasi, deployment, dan pemantauan. Buat batas antar tahap eksplisit agar masing-masing dapat diuji, dicoba ulang, dan diaudit. Hindari kegagalan umum di mana model dilatih di notebook ad hoc dan dilempar melewati tembok ke operasi. Sebagai gantinya, bungkus siklus hidup dalam pipeline terorkestrasi yang dapat dijalankan insinyur berwenang mana pun dari checkout bersih.

### Pakai feature store, pelacakan eksperimen, dan registri model

**Feature store** memusatkan definisi fitur agar transformasi yang sama berjalan baik dalam pelatihan maupun penyajian. Ini menghilangkan training-serving skew (ketidakkonsistenan antara cara fitur dihitung untuk pelatihan dan untuk prediksi langsung) dan memungkinkan tim menggunakan ulang fitur alih-alih menghitung ulang. **Pelacakan eksperimen** mencatat parameter, versi kode, versi data, dan metrik setiap proses pelatihan, agar hasil dapat dibandingkan dan direproduksi. **Registri model** adalah sistem pencatat untuk model terlatih, menyimpan versi, silsilah, hasil evaluasi, status persetujuan, dan tahap deployment. Bersama-sama, ini memungkinkan Anda menjawab "apa yang berubah?" ketika perilaku bergeser, dan mempromosikan atau me-rollback model melalui tahap yang diatur.

### Jadikan data dan model dapat direproduksi dan diversikan dengan silsilah

Versikan dataset Anda, bukan hanya kode. Pakai penyimpanan beralamat-konten atau perkakas versioning data agar proses pelatihan merujuk ke snapshot tak berubah. Sematkan kode dengan commit git, dan sematkan lingkungan dengan dependensi terkunci dan citra kontainer. Tangkap silsilah ujung ke ujung: data mentah mana memberi makan fitur mana, fitur dan kode mana menghasilkan model mana, dan di mana model itu di-deploy. Ketika insiden atau audit datang, silsilah mengubah mimpi buruk forensik menjadi kueri sederhana. Catat keacakan (seed) dan perangkat keras di mana pun hasil bergantung padanya.

### Pilih pola deployment yang sesuai beban kerja

- **Batch** memberi skor sesuai jadwal atas dataset besar; paling sederhana dioperasikan, toleran terhadap latensi, ideal untuk laporan dan keputusan berkala.
- **Online (real-time)** menyajikan respons untuk permintaan individual dalam anggaran latensi ketat; butuh pengambilan fitur berlatensi rendah dan perencanaan kapasitas cermat.
- **Streaming** memberi skor peristiwa terus-menerus saat tiba; cocok untuk deteksi penipuan dan pemantauan di mana kesegaran kritis.
- **Edge** menjalankan model pada perangkat atau perangkat keras on-premises demi latensi, privasi, konektivitas, atau alasan kedaulatan data, lazim di pemerintah dan lingkungan lapangan.

Pilih pola paling sederhana yang memenuhi persyaratan, dan rancang peluncuran Anda dengan deployment shadow, canary, dan rollback instan.

### Pantau drift, degradasi, dan kualitas data

Instrumentasi masukan dan keluaran di produksi. Awasi **data drift** (distribusi masukan bergeser), **[concept drift](https://en.wikipedia.org/wiki/Concept_drift)** (hubungan antara masukan dan target berubah), kegagalan **kualitas data** (null, perubahan skema, sumber hulu rusak), dan **degradasi kinerja** yang diukur terhadap ground truth tertunda di mana Anda memilikinya. Tetapkan ambang peringatan, tulis runbook, dan sambungkan pemantauan ke pemicu pelatihan ulang Anda. Degradasi senyap adalah mode kegagalan ML klasik, dan pemantauan adalah satu-satunya pertahanan Anda terhadapnya.

## Trade-off: kelebihan dan kekurangan

| Keputusan | Opsi A | Opsi B | Trade-off |
|---|---|---|---|
| Pola penyajian | Batch | Online | Kesederhanaan dan biaya versus kesegaran dan latensi |
| Komputasi fitur | Feature store | Pipeline per model | Konsistensi dan penggunaan ulang versus overhead penyiapan |
| Platform | Beli platform MLOps terkelola | Rakit perkakas open-source | Kecepatan dan dukungan versus fleksibilitas dan lock-in |
| Pelatihan ulang | Terjadwal | Dipicu drift | Keterprediksian versus responsivitas dan kompleksitas |
| Ketelitian reprodusibilitas | Versioning data penuh | Pelacakan ringan | Kekuatan audit versus penyimpanan dan upaya |

Trade-off menyeluruhnya adalah investasi sekarang versus kerapuhan kelak. Infrastruktur reprodusibilitas dan pemantauan berat menelan upaya di muka, tetapi mencegah biaya jauh lebih besar dari kegagalan tak terjelaskan, model tak dapat direproduksi, dan kepercayaan yang terkikis. Platform terkelola mempercepat tim tetapi dapat menciptakan lock-in; tumpukan open-source menawarkan kendali dengan harga kerja integrasi. Organisasi besar biasanya diuntungkan oleh tim platform bersama yang menyembunyikan kompleksitas ini di balik bawaan jalan-beraspal.

## Pertanyaan untuk didiskusikan dengan tim Anda

1. **Bagaimana kita akan mengetahui model ter-deploy telah memburuk secara senyap sebelum pelanggan atau warga dirugikan, dan siapa yang memiliki peringatan itu?** Pembusukan senyap adalah mode kegagalan ML klasik: kode masih berjalan, model masih mengembalikan skor yakin, dan kualitas merosot seiring dunia menyimpang dari data pelatihan. Bagi tim besar yang menjalankan banyak model, Anda butuh ini terjawab per model, bukan sekali untuk armada, karena masing-masing punya profil drift sendiri dan penundaan ground-truth sendiri. Bawa pemantau Anda saat ini untuk data drift, concept drift, dan kerusakan kualitas data, ambang peringatan, dan runbook yang menyatakan siapa yang merespons. Dalam pengaturan teregulasi di mana label tiba berminggu-minggu terlambat, diskusikan sinyal proksi yang dapat diawasi sementara itu, karena menunggu ground truth tertunda berarti menunggu untuk menemukan kerugian. Jika tak ada pemilik tunggal yang dinamai untuk peringatan drift sebuah model, model itu secara efektif tidak dipantau.

2. **Jika auditor meminta kita mereproduksi prediksi spesifik dari delapan belas bulan lalu, dapatkah kita benar-benar melakukannya ujung ke ujung?** Reprodusibilitas adalah persyaratan kepatuhan yang bersembunyi di dalam rekayasa baik: ia memungkinkan lembaga menjawab persisnya model mana, dilatih pada data mana, dengan kode mana, menghasilkan keputusan yang memengaruhi seseorang. Bawa contoh nyata dan coba telusuri: snapshot data tak berubah, commit git, dependensi terkunci dan citra kontainer, seed tercatat, dan silsilah dari data mentah melalui fitur ke model ter-deploy. Sinyalnya adalah apakah ada mata rantai dalam rantai itu yang hilang atau manual. Untuk pemerintah dan industri teregulasi, putuskan masa retensi yang benar-benar dipersyaratkan hukum dan pastikan penyimpanan Anda menjaga silsilah tetap dapat dijawab selama seluruh jendela itu, karena celah mengubah kueri rutin menjadi darurat forensik.

3. **Apa aturan kita untuk mempromosikan model ke produksi dan me-rollback-nya, dan apakah ditegakkan oleh registri atau hanya oleh kepercayaan?** Promosi tanpa tata kelola adalah cara eksperimen notebook bocor ke produksi dan cara model buruk bertahan karena tak ada yang dapat mengembalikannya dengan bersih. Bagi banyak tim, beda antara matang dan rapuh adalah apakah registri model menggerbangi promosi dengan persetujuan dan evaluasi wajib, atau apakah insinyur dapat mendorong bobot dengan tangan. Bawa jalur promosi Anda saat ini, mekanisme rollback Anda, dan bukti bahwa deployment shadow atau canary benar-benar berjalan sebelum lalu lintas penuh. Diskusikan apakah pelatihan ulang terjadwal atau dipicu drift, dan apakah model hasil pelatihan ulang lolos gerbang validasi sebelum deployment, karena melatih ulang pada data langsung tanpa validasi memperkuat drift atau peracunan. Jawabannya harus ditegakkan dalam platform, bukan dalam halaman wiki yang dipercayakan untuk diikuti orang.

4. **Apakah kita membangun platform MLOps di atas perkakas open-source, membeli yang terkelola, atau memadukan keduanya, dan siapa yang telah menimbang lock-in?** Pilihan ini menetapkan langit-langit seberapa cepat setiap model masa depan dikirim dan seberapa banyak kendali yang Anda pertahankan atas data dan pipeline. Platform terkelola membawa tim ke produksi dengan cepat dan menanggung dukungan, tetapi dapat menjebak definisi fitur, catatan silsilah, dan artefak model Anda dalam format proprietari yang tak mudah ditinggalkan; tumpukan open-source rakitan menjaga Anda portabel dengan harga kerja integrasi dan pemeliharaan nyata. Bawa total biaya kepemilikan untuk setiap jalur (lisensi atau bangun, penyimpanan, komputasi untuk pelatihan ulang, dan staf platform untuk mengoperasikannya), pembacaan jujur atas kapasitas tim Anda menjalankan infrastruktur, dan uji keluar konkret: dapatkah Anda mengekspor registri, feature store, dan silsilah lalu membangun ulang di tempat lain? Dalam pengaturan enterprise dan pemerintah, tambahkan kendala pengadaan dan aturan kedaulatan data, karena platform yang menyimpan data pelatihan di wilayah atau format yang dilarang regulator Anda didiskualifikasi seberapa pun nyamannya.

5. **Haruskah feature store dan registri model kita menjadi satu platform terpusat atau terfederasi per tim, dan berapa biaya training-serving skew bagi kita hari ini?** Memusatkan definisi fitur menghilangkan skew di mana fitur dihitung satu cara dalam pelatihan dan cara lain dalam penyajian, sumber hilangnya akurasi yang senyap dan mahal, tetapi platform tunggal dapat menjadi hambatan yang memperlambat setiap tim. Federasi memberi tim otonomi sambil melipatgandakan perpipaan dan peluang dua tim mendefinisikan fitur yang sama secara tidak konsisten. Bawa bukti di mana skew sudah menggigit Anda, berapa banyak tim menggunakan ulang fitur versus membangun ulang, dan bawaan jalan-beraspal yang dapat ditawarkan tim platform bersama. Untuk organisasi besar, timbang manfaat tata kelola satu sistem pencatat yang dapat diaudit terhadap biaya pengiriman antrean pusat, dan dalam pengaturan teregulasi pilih silsilah terpusat yang memungkinkan auditor menelusuri prediksi apa pun ke kode fitur persis yang menghasilkannya.

6. **Sudahkah kita mencocokkan pola deployment setiap model dengan kebutuhan latensi, kesegaran, dan kedaulatan sebenarnya, atau menjadikan semuanya satu bentuk secara bawaan?** Batch, online, streaming, dan edge masing-masing membawa biaya operasional dan kompleksitas yang sangat berbeda, dan memilih yang salah entah menghabiskan berlebihan untuk infrastruktur real-time yang tak pernah dibutuhkan laporan malam atau membuat pemberi skor penipuan kelaparan kesegaran yang menjadi sandarannya. Putuskan per beban kerja pola mana yang benar-benar dibenarkan persyaratan, dan tolak membakukan pada opsi paling kompleks karena terasa modern. Bawa anggaran latensi, volume, biaya jawaban basi, dan penundaan ground-truth untuk setiap model. Di pemerintah dan lingkungan lapangan, timbang deployment edge dan on-premises dengan sengaja, karena aturan kedaulatan data atau konektivitas terputus-putus dapat memaksa model ke perangkat keras lokal, dan pilihan itu membentuk ulang cara Anda memversikan, memantau, dan me-rollback setiap model yang Anda dorong ke sana.

## Lensa sektor

**Startup.** Sumber daya Anda yang paling langka adalah perhatian rekayasa, jadi jaga MLOps ringan dan belilah. Lacak eksperimen di perkakas ter-hosting sederhana, sematkan setiap model ter-deploy ke snapshot data pelatihan dan commit kodenya di git, dan tambah satu pemeriksaan drift murah alih-alih platform. Lewati feature store dan pipeline pesanan sampai model kedua atau ketiga membuat penggunaan ulang layak; tumpukan rapuh yang tak dapat Anda pelihara akan menenggelamkan Anda lebih cepat daripada kemampuan yang hilang.

**Bisnis kecil.** Anda kemungkinan tidak punya spesialis platform ML dan anggaran ketat, jadi perlakukan MLOps sebagai sesuatu yang tertanam dalam perkakas yang sudah Anda jalankan, bukan sistem yang Anda isi stafnya. Pilih layanan terkelola yang menangani versioning, deployment, dan pemantauan untuk Anda, dan bingkai disiplin ini sebagai pertanyaan kebersihan data dan reprodusibilitas: ketahui model dan data mana yang menghasilkan hasil tertentu, dan pertahankan kemampuan rollback. Pilih vendor yang membiarkan Anda mengekspor data dan model agar peralihan kelak tetap mungkin.

**Enterprise.** Masalahnya skala di puluhan model dan banyak tim: feature store bersama, pelacakan eksperimen, dan registri model dengan promosi yang diatur agar kelompok berhenti menciptakan ulang pipeline. Anggarkan tim platform yang menawarkan bawaan jalan-beraspal, bakukan silsilah dan pemantauan agar setiap model dapat diaudit dan setiap insiden dapat dijelaskan, dan kelola bangun-versus-beli dan lock-in dengan sengaja di balik antarmuka yang menjaga perkakas di bawahnya tetap dapat ditukar. Tegakkan gerbang validasi dan rollback dalam platform, bukan dalam konvensi.

**Pemerintah.** Reprodusibilitas, silsilah, dan versioning adalah persyaratan kepatuhan yang menyamar, jadi perlakukan sebagai kelas satu sejak hari pertama. Versikan dataset dan kode persis di balik setiap model ter-deploy, pertahankan silsilah itu selama masa yang dipersyaratkan hukum, dan mampu mereproduksi prediksi historis apa pun yang memengaruhi warga. Jaga manusia meninjau keputusan berdampak, timbang deployment edge dan on-premises di mana aturan kedaulatan data menuntutnya, dan wajibkan platform vendor mana pun memberi portabilitas penuh atas data, fitur, dan silsilah Anda.

## Contoh

**Startup.** Startup analitik kecil mengirim model prediksi churn pertamanya dengan satu ilmuwan data dan penyiapan ringan. Ia melacak eksperimen di perkakas ter-hosting sederhana, menyematkan setiap model ter-deploy ke snapshot data pelatihan dan commit kodenya di git, dan menambah pekerjaan mingguan dasar yang membandingkan masukan terbaru dengan distribusi pelatihan. Ketika sumber data mengubah format tanggalnya dan prediksi mulai menyimpang, pemeriksaan sederhana itu menangkapnya dalam hitungan hari alih-alih setelah telepon pelanggan marah, dan tim dapat mereproduksi model baik terakhir lalu me-rollback.

**Enterprise.** Sebuah bank ritel menjalankan puluhan model kredit dan penipuan. Ia membakukan feature store yang dibagi lintas tim, layanan pelacakan eksperimen, dan registri model dengan gerbang persetujuan wajib. Setiap model di produksi dapat ditelusuri ke snapshot data pelatihan dan commit kodenya. Model penipuan di-deploy sebagai pemberi skor streaming; model kredit berjalan batch. Lapisan pemantauan mengawasi drift masukan dan memberi peringatan ketika skema sumber data berubah, yang pernah menangkap umpan hulu rusak sebelum merusak keputusan.

**Pemerintah.** Sebuah lembaga tunjangan publik memakai model ML untuk memprioritaskan tinjauan kasus. Karena keputusan itu memengaruhi akses warga ke layanan, lembaga memversikan dataset dan kode persis di balik setiap model ter-deploy, menyimpan silsilah ini selama masa yang dipersyaratkan hukum, dan dapat mereproduksi prediksi historis apa pun atas permintaan. Model di-deploy batch dengan manusia meninjau kasus yang ditandai, dan pemantau drift memaksa evaluasi ulang wajib setiap kali populasi masuk bergeser, sehingga model tak pernah diam-diam diterapkan di luar kondisi tempat ia divalidasi.

## Kasus bisnis: motivasi, ROI, dan TCO

MLOps membayar dirinya sendiri dengan mengubah eksperimen rapuh menjadi aset yang dapat diandalkan. ROI datang dari waktu-ke-produksi lebih cepat untuk model baru, insiden mahal lebih sedikit, infrastruktur duplikat lebih sedikit, dan kemampuan mengoperasikan banyak model dengan tim platform kecil. Feature store dan registri bersama dapat memangkas waktu pengiriman per model secara dramatis, karena tim berhenti membangun ulang perpipaan yang sama.

TCO mencakup bangun atau lisensi platform, penyimpanan untuk data dan model yang diversikan, komputasi untuk pelatihan ulang, dan staf untuk mengoperasikan semuanya. Timbang itu terhadap biaya tidak mengadopsi: model yang tak dapat Anda reproduksi atau audit, kegagalan senyap yang merugikan pelanggan atau warga, dan temuan regulasi. Dalam pengaturan teregulasi, biaya model tak terjelaskan dalam audit dapat melampaui seluruh investasi MLOps. Ajukan kasus kepada pimpinan dengan membingkai MLOps sebagai pengurangan risiko dan percepatan pengiriman, bukan overhead: jalan beraspal yang akan dilalui setiap model masa depan.

## Anti-pola dan jebakan

- **Lompatan notebook-ke-produksi.** Men-deploy model yang dilatih di notebook tanpa tata kelola tanpa reprodusibilitas.
- **Training-serving skew.** Kode fitur berbeda dalam pelatihan dan penyajian, menyebabkan hilangnya akurasi senyap.
- **Tanpa versioning data.** Memversikan kode tetapi tidak data, sehingga proses tak dapat direproduksi.
- **Deploy lalu lupakan.** Mengirim model tanpa pemantauan, menemukan degradasi hanya ketika pengguna mengeluh.
- **Pelatihan ulang otopilot.** Melatih ulang otomatis pada data langsung tanpa validasi, memperkuat drift atau peracunan.
- **Infrastruktur sekali pakai.** Setiap tim membangun pipeline sendiri, melipatgandakan biaya dan kerapuhan.
- **Mengabaikan label tertunda.** Mengasumsikan Anda dapat mengukur akurasi seketika ketika ground truth tiba berminggu-minggu kemudian.

## Model kematangan

1. **Memulai.** Model dibangun ad hoc di notebook; deployment manual; tanpa versioning data atau model; tanpa pemantauan; mereproduksi prediksi masa lalu adalah terkaan.
2. **Mengembangkan.** Sebagian pelacakan eksperimen dan registri model muncul, tetapi praktik bervariasi menurut tim; deployment semi-otomatis; pemantauan dasar mencakup beberapa model; versioning data parsial dan silsilah punya celah.
3. **Membakukan.** Platform bersama dengan feature store, registri, pipeline yang dapat direproduksi, dan silsilah ujung ke ujung didokumentasikan dan ditegakkan di seluruh organisasi; pemantauan drift dan kualitas data berjalan di seluruh model; promosi dan rollback mengikuti jalur teratur yang dipakai setiap tim.
4. **Mengelola.** Armada diukur terhadap garis dasar: tingkat drift, kerusakan kualitas data, akurasi model terhadap ground truth tertunda, training-serving skew, waktu-ke-produksi, dan biaya operasi per model dilacak sebagai metrik; ambang peringatan dan gerbang validasi ditegakkan atas bukti, dan kesehatan setiap model ditinjau pada irama tetap dengan pemilik bernama.
5. **Mengorkestrasi.** Siklus hidup sepenuhnya otomatis, dapat diaudit, dan adaptif; pelatihan ulang dipicu drift berjalan di balik gerbang validasi; jalan beraspal swalayan memungkinkan tim mengirim dengan aman; evaluasi berkelanjutan mengikat kinerja model ke metrik bisnis, dan platform terintegrasi dengan pengiriman, risiko, dan kepatuhan sehingga model rutin dipensiunkan, diganti, dan ditentukan ulang cakupannya seiring data dan kondisi bergeser.

## Gagasan untuk didiskusikan

- Bagaimana Anda menyeimbangkan kebebasan eksperimen dengan reprodusibilitas produksi?
- Apa pemicu pelatihan ulang yang tepat (jadwal, drift, atau penurunan kinerja) untuk kasus penggunaan Anda?
- Berapa lama Anda harus menyimpan silsilah data dan model, dan apa yang mendorong persyaratan itu?
- Haruskah feature store dan registri menjadi platform terpusat atau terfederasi per tim?
- Bagaimana Anda memantau akurasi ketika label ground-truth tiba dengan penundaan panjang?
- Kapan deployment edge layak untuk kompleksitas operasional tambahannya?

## Poin-poin utama

- Perilaku ML datang dari kode ditambah data ditambah model; versikan dan atur ketiganya bersama.
- Feature store, pelacakan eksperimen, dan registri adalah tulang punggung ML yang dapat direproduksi.
- Silsilah membuat model dapat diaudit dan insiden dapat dijelaskan: esensial dalam pengaturan teregulasi.
- Pilih batch, online, streaming, atau edge agar sesuai kebutuhan latensi, kesegaran, dan kedaulatan.
- Model memburuk; pemantauan drift, kualitas data, dan peluruhan bukan opsional.

## Referensi dan bacaan lanjutan

- Chip Huyen, *Designing Machine Learning Systems*.
- Andriy Burkov, *Machine Learning Engineering*.
- D. Sculley et al., *Hidden Technical Debt in Machine Learning Systems*.
- Mark Treveil et al., *Introducing MLOps*.
- Valliappa Lakshmanan, Sara Robinson, dan Michael Munn, *Machine Learning Design Patterns*.
- Emmanuel Ameisen, *Building Machine Learning Powered Applications*.
