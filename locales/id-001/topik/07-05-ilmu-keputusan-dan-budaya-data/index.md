# 7.5 Ilmu keputusan dan budaya berbasis data

## Tinjauan dan motivasi

Ilmu keputusan adalah praktik menghubungkan data dengan keputusan nyata, memanfaatkan statistik, ilmu perilaku, dan penilaian untuk membantu orang memilih dengan baik di bawah ketidakpastian. Budaya berbasis data adalah kondisi organisasi di mana hal ini terjadi secara bawaan: orang meraih bukti, bernalar cermat tentang sebab-akibat, mengomunikasikan ketidakpastian dengan jujur, dan memperbarui keyakinan ketika data menjamin. Bab ini sengaja menjadi puncak urutan data, karena semua strategi, rekayasa, analitik, dan eksperimen yang mendahuluinya tak berharga jika tidak mengubah keputusan menjadi lebih baik.

Bagi tim besar, inilah tempat investasi data paling sering gagal, bukan di pipeline melainkan di mil terakhir dari wawasan ke tindakan. Enterprise menghabiskan banyak untuk platform dan dasbor namun tetap membuat keputusan besar lewat hierarki, kebiasaan, atau pemaparan paling percaya diri. Mode kegagalan umum adalah sandiwara data: dasbor dan analisis rumit yang dibuat agar tampak teliti sementara keputusan sebenarnya sudah dibuat di muka dan data dipetik selektif untuk membenarkannya. Pemerintah menambah taruhan tinggi dan pengawasan. Keputusan kebijakan yang dibenarkan klaim kausal lemah dapat salah mengalokasikan uang publik dan merugikan warga, dan tuntutan akuntabilitas menjadikan penalaran jujur tentang bukti kewajiban sipil, bukan sekadar praktik baik.

Masalah sulit di sini bersifat kognitif dan budaya, bukan teknis. Orang mencampuradukkan [korelasi dengan kausalitas](https://en.wikipedia.org/wiki/Correlation_does_not_imply_causation), mengabaikan [confounder](https://en.wikipedia.org/wiki/Confounding) (variabel tersembunyi yang mendorong baik penyebab yang diduga maupun efeknya), berjangkar pada angka pertama yang mereka lihat, dan membaca estimasi titik sebagai kepastian. Dan dalam dorongan menjadi digerakkan data, organisasi dapat hanyut ke pengawasan: mengukur individu begitu mengganggu sehingga merusak kepercayaan dan memancing manipulasi. Membangun budaya pengukuran sejati berarti menata penalaran dengan benar, mengomunikasikan ketidakpastian dengan setia, dan mengukur sistem serta hasil tanpa mengubah data menjadi alat kendali atas orang.

## Prinsip utama

- Tujuan data adalah keputusan lebih baik, bukan produksi laporan.
- Putuskan apa yang akan mengubah pikiran Anda sebelum melihat data.
- Korelasi bukan kausalitas; interogasi confounder sebelum bertindak.
- Komunikasikan ketidakpastian dengan jujur; estimasi titik tanpa rentang menyesatkan.
- Jadilah berbasis data, bukan diperbudak data; penilaian dan konteks tetap penting.
- Ukur untuk belajar dan memperbaiki sistem, bukan untuk mengawasi dan menghukum individu.
- Perbarui keyakinan ketika bukti menjamin; mengubah pikiran adalah kekuatan.
- [Keamanan psikologis](https://en.wikipedia.org/wiki/Psychological_safety) adalah prasyarat bagi analisis jujur dan perbedaan pendapat.

## Rekomendasi

### Hubungkan data dengan keputusan dan hindari sandiwara data

Ikat analisis pada keputusan spesifik sejak awal: apa yang akan kita lakukan berbeda tergantung pada apa yang kita temukan? Sebelum mengumpulkan data, nyatakan keputusan, opsi, dan bukti apa yang mendukung masing-masing, idealnya hasil apa yang akan mengubah pikiran Anda. Ini menjaga dari sandiwara data, di mana analisis sekadar menghiasi keputusan yang sudah dibuat. Jika tak ada temuan realistis yang akan mengubah pilihan, jangan habiskan uang untuk analisis. Buat penilaian dengan jujur dan katakan demikian. Desak agar presentasi dimulai dengan keputusan dan rekomendasi, bukan tur bagan.

### Bernalar cermat tentang kausalitas

Sebagian besar pertanyaan bisnis dan kebijakan bersifat kausal (apakah tindakan ini akan menghasilkan hasil ini), tetapi sebagian besar data yang tersedia bersifat observasional dan penuh confounder. Ajari tim perbedaan korelasi dan kausalitas, serta jebakannya: variabel pengganggu, [bias seleksi](https://en.wikipedia.org/wiki/Selection_bias), kausalitas terbalik, dan korelasi palsu. Pilih eksperimen acak untuk klaim kausal di mana layak. Di mana eksperimen mustahil, pakai teknik [inferensi kausal](https://en.wikipedia.org/wiki/Causal_inference) yang cermat dan nyatakan asumsi Anda secara eksplisit alih-alih meluncur dari "berasosiasi dengan" ke "menyebabkan." Waspadai terutama cerita meyakinkan yang dibangun di atas satu korelasi.

### Komunikasikan ketidakpastian kepada pemangku kepentingan

Angka yang disajikan sebagai estimasi titik presisi mengundang keyakinan palsu. Komunikasikan rentang, interval kepercayaan atau kredibel, dan asumsi kunci di balik angka mana pun. Pakai bahasa sederhana dan visual jujur (batang galat, rentang, pita skenario) agar pengambil keputusan memahami apa yang diketahui dan tidak diketahui. Bedakan apa yang ditunjukkan data, apa yang Anda simpulkan, dan apa yang Anda asumsikan. Kalibrasi keyakinan terhadap bukti: sajikan perkiraan dari data tipis persis sebagai itu. Ketidakpastian yang dikomunikasikan dengan jujur membangun lebih banyak kepercayaan daripada presisi palsu, karena ia selamat dari sentuhan dengan kenyataan.

### Bangun budaya pengukuran tanpa pengawasan

Ciptakan lingkungan di mana tim rutin mendefinisikan metrik keberhasilan, mengukur hasil, dan belajar darinya, tetapi arahkan pengukuran pada sistem, proses, dan hasil alih-alih memantau individu. Metrik yang dipakai untuk mengawasi dan memeringkat orang dimanipulasi, melahirkan ketakutan, dan merusak kejujuran yang dibutuhkan keputusan baik (dinamika yang ditangkap oleh [hukum Goodhart](https://en.wikipedia.org/wiki/Goodhart's_law): ukuran yang menjadi target berhenti menjadi ukuran yang baik). Pilih metrik agregat berorientasi hasil. Libatkan tim dalam memilih ukuran mereka sendiri, dan pisahkan metrik pembelajaran dari evaluasi kinerja. Lindungi keamanan psikologis agar orang mengungkap kabar buruk dan perbedaan pendapat sejak dini.

### Tumbuhkan kebiasaan dan literasi data yang sehat

Tingkatkan literasi data secara luas agar orang dapat membaca bagan secara kritis, mempertanyakan definisi metrik, dan melihat klaim menyesatkan. Normalkan bertanya "bagaimana kita tahu itu?" dan "apa yang akan mengubah pikiran kita?" Hargai orang yang memperbarui pandangan mereka berdasarkan bukti dan yang menjalankan eksperimen yang gagal secara informatif. Buat aman untuk mengatakan "data tidak memberi tahu kita" alih-alih mengarang kepastian. Pemimpin menetapkan nada: ketika mereka mengubah keputusan berdasarkan bukti dan mengakui ketidakpastian, budaya mengikuti.

### Jaga dari bias dan penyalahgunaan

Awasi bias yang dapat diprediksi: [bias konfirmasi](https://en.wikipedia.org/wiki/Confirmation_bias) dalam memilih data pendukung, [bias penyintas](https://en.wikipedia.org/wiki/Survivorship_bias) dalam mengabaikan apa yang hilang, berjangkar pada angka awal, dan bias tinjauan belakang dalam postmortem. Bangun tinjauan advokat iblis, pra-registrasi apa yang Anda harapkan temukan, dan perspektif beragam pada analisis penting. Perlakukan etika data dengan serius (keadilan, transparansi, dan menghindari kerugian), terutama ketika keputusan memengaruhi mata pencarian, tunjangan, atau hak orang.

## Trade-off: kelebihan dan kekurangan

| Pilihan | Kelebihan | Kekurangan | Paling cocok |
|---|---|---|---|
| Digerakkan data (data memutuskan) | Mengurangi bias, konsisten | Mengabaikan konteks, dimanipulasi, rapuh | Ranah yang dipahami baik |
| Berbasis data (data plus penilaian) | Menyeimbangkan bukti dan konteks | Lebih lambat, butuh penilaian | Keputusan kompleks atau baru |
| Eksperimen untuk kausalitas | Bukti kausal kuat | Mahal, lambat, tak selalu layak | Pilihan berisiko tinggi yang dapat dibalik |
| Inferensi observasional | Memakai data yang tersedia | Risiko confounding, klaim lebih lemah | Ketika eksperimen mustahil |
| Metrik hasil/sistem | Mendorong perbaikan, manipulasi rendah | Akuntabilitas individu lebih sedikit | Budaya pembelajaran |
| Pengawasan individu | Visibilitas granular | Manipulasi, ketakutan, kepercayaan terkikis | Jarang dibenarkan |

Ketegangan penentunya adalah ketelitian versus kecepatan dan kelayakan. Eksperimen acak memberi bukti kausal terkuat, tetapi memakan waktu dan sering mustahil untuk pilihan strategis atau kebijakan sekali jalan, di mana penilaian cermat tentang confounder dan asumsi eksplisit harus memadai. Ketegangan kedua antara pengukuran dan kepercayaan: semakin granular Anda mengukur individu, semakin banyak yang dapat Anda lihat dan semakin sedikit perilaku jujur yang Anda dapatkan. Budaya matang condong ke penilaian berbasis data dan pengukuran agregat berorientasi hasil. Ia menerima presisi tampak yang sedikit lebih rendah sebagai ganti keputusan yang bertahan dan tenaga kerja yang mengatakan kebenaran.

## Pertanyaan untuk didiskusikan dengan tim Anda

1. **Apakah Anda menyatakan apa yang akan mengubah pikiran Anda sebelum melihat data, dan apakah pertanyaan itu tertulis dalam dokumen keputusan Anda?** Penjaga terkuat bab ini terhadap sandiwara data adalah menamai keputusan, opsi, dan bukti yang akan mendukung masing-masing, idealnya hasil yang akan membalik pilihan Anda, sebelum mengumpulkan data. Jika tak ada temuan realistis yang akan mengubah keputusan, langkah jujur adalah melewatkan analisis dan membuat penilaian secara terbuka. Bagi enterprise dan lembaga di mana satu pilihan strategis atau kebijakan dapat memboroskan lebih dari biaya seluruh program analitik, disiplin ini berdaya ungkit tinggi. Bawa keputusan terbaru dan tanyakan apakah temuan apa pun dapat mengubahnya, atau apakah bagan sekadar menghiasi kesimpulan yang sudah dicapai. Jika "apa yang akan mengubah pikiran kita?" bukan petunjuk standar dalam dokumen keputusan Anda, jadikan demikian, dan desak presentasi dimulai dengan rekomendasi, bukan tur bagan.

2. **Ketika korelasi meyakinkan muncul, bagaimana Anda menginterogasi confounder sebelum bertindak, dan apakah Anda memilih eksperimen di mana layak?** Bab ini memperingatkan bahwa sebagian besar pertanyaan bisnis dan kebijakan bersifat kausal sementara sebagian besar data yang tersedia observasional dan penuh confounder, bias seleksi, dan kausalitas terbalik. Contohnya sendiri mengulang satu jebakan: pelanggan yang terlibat memilih sendiri masuk ke fitur atau program, sehingga korelasi mentah dengan churn lebih rendah atau penemuan kerja lebih tinggi lenyap di bawah perbandingan terkendali. Bertindak atas korelasi itu berarti kampanye atau kebijakan mahal yang salah arah. Bawa keputusan terbaru yang bertumpu pada satu korelasi dan tanyakan variabel tersembunyi apa yang dapat mendorong kedua sisi. Di mana eksperimen layak, pilih itu; di mana tidak, pakai metode inferensi kausal yang cermat dan nyatakan asumsi Anda secara eksplisit alih-alih meluncur dari "berasosiasi dengan" ke "menyebabkan."

3. **Apakah metrik Anda diarahkan untuk memperbaiki sistem dan hasil, atau memantau individu, dan sudahkah Anda memisahkan metrik pembelajaran dari evaluasi kinerja?** Bab ini menarik garis tegas: pengukuran yang diarahkan pada orang dimanipulasi, melahirkan ketakutan, dan merusak kejujuran yang dibutuhkan keputusan baik, dinamika yang diprediksi hukum Goodhart begitu ukuran menjadi target. Ia mengutamakan metrik agregat berorientasi hasil, melibatkan tim dalam memilih ukuran mereka sendiri, dan melindungi keamanan psikologis agar orang mengungkap kabar buruk lebih awal. Dalam pengaturan pemerintah dan enterprise, mengawasi staf garis depan mengikis kepercayaan yang membuat data akurat mungkin sejak awal. Bawa pertanyaan konkret: metrik Anda yang mana dapat dipakai untuk memeringkat atau menghukum individu, dan akankah orang memanipulasinya di bawah tekanan? Jika metrik pembelajaran dan evaluasi kinerja terjalin, pisahkan, agar pengukuran mendorong perbaikan alih-alih perilaku defensif.

4. **Ketika angka mencapai pengambil keputusan, apakah ia tiba sebagai rentang dengan asumsinya terlampir, atau sebagai estimasi titik yang mengundang keyakinan palsu?** Bab ini berargumen bahwa ketidakpastian yang dikomunikasikan dengan jujur membangun lebih banyak kepercayaan daripada presisi palsu, karena ia selamat dari sentuhan dengan kenyataan, namun tarikan menuju satu angka yakin kuat ketika pemimpin menginginkan jawaban bersih. Bagi tim besar, tekanan yang bersaing nyata: rentang dan batang galat dapat terbaca mengelak bagi eksekutif yang menghargai ketegasan, sehingga analis belajar membuang peringatan agar didengar. Bawa laporan terbaru dan periksa apakah ia membedakan apa yang ditunjukkan data, apa yang Anda simpulkan, dan apa yang Anda asumsikan, dan apakah perkiraan dari data tipis diberi label persis sebagai itu. Dalam pengaturan enterprise dan pemerintah, di mana angka dapat berakhir di paket dewan, pengajuan anggaran, atau kesaksian publik, estimasi titik yang disajikan sebagai kepastian adalah liabilitas, jadi sepakati standar rumah bahwa angka berdampak membawa rentang, asumsi kunci, dan pernyataan jelas tentang keyakinan.

5. **Apakah benar-benar aman di sini untuk mengatakan "data tidak memberi tahu kita," dan siapa yang diizinkan menantang cara metrik didefinisikan?** Bab ini memperlakukan literasi data dan keamanan psikologis sebagai prasyarat: orang perlu membaca bagan secara kritis, bertanya "bagaimana kita tahu itu?", dan mengakui ketidakpastian tanpa hukuman, atau budaya mengarang kepastian palsu secara bawaan. Ketegangan bagi organisasi besar adalah literasi luas butuh waktu pelatihan dan anggaran nyata, dan mempertanyakan metrik favorit orang senior dapat terasa membatasi karier, sehingga angka tak diperiksa naik ke atas tanpa tantangan. Bawa bukti siapa di ruangan yang benar-benar dapat menginterogasi definisi dan asal-usul metrik, dan ingat kapan terakhir seseorang dihargai alih-alih dihukum karena memperbarui pandangan atau melaporkan kegagalan informatif. Bagi badan enterprise dan pemerintah, di mana ukuran yang didefinisikan buruk dapat menggerakkan pendanaan atau pelaporan publik, namai secara eksplisit siapa yang berhak mempertanyakan metrik dan lindungi mereka ketika menggunakannya.

6. **Bagaimana Anda menjaga analisis penting dari bias yang dapat diprediksi, dan apakah Anda membangun perbedaan pendapat sebelum keputusan alih-alih sesudahnya?** Bab ini mendaftar jebakan yang diam-diam merusak bukti: bias konfirmasi dalam memilih data pendukung, bias penyintas dalam mengabaikan apa yang hilang, berjangkar pada angka awal, dan bias tinjauan belakang dalam postmortem. Pertimbangan yang bersaing adalah kecepatan, karena tinjauan advokat iblis, pra-registrasi apa yang Anda harapkan temukan, dan perspektif beragam semuanya memperlambat keputusan dan menjadi yang pertama dipotong di bawah tekanan tenggat. Bawa analisis berisiko tinggi terbaru dan tanyakan apa yang akan muncul jika seseorang ditugasi membantah kasus sebaliknya, dan apakah tim menuliskan ekspektasinya sebelum melihat hasil. Dalam konteks enterprise dan terutama pemerintah, di mana keputusan memengaruhi mata pencarian, tunjangan, atau hak orang, perlakukan etika data dan perbedaan pendapat terstruktur sebagai persyaratan tetap pada analisis berdampak, bukan tambahan yang dapat dijatuhkan diam-diam oleh kuartal yang sibuk.

## Lensa sektor

**Startup.** Tanpa analis dan hanya beberapa minggu runway per taruhan, ilmu keputusan Anda adalah satu kebiasaan, bukan fungsi: sebelum komitmen besar, tanyakan hasil apa yang akan mengubah pikiran Anda dan apakah eksperimen murah dapat menjawabnya lebih cepat daripada rapat. Jaga keras agar tidak mempertaruhkan kuartal pada satu korelasi mencolok, karena tim kecil tak dapat pulih dari peta jalan yang salah arah. Jaga tetap ringan, satu baris tertulis dalam dokumen keputusan yang menamai sinyal yang akan membuat Anda berhenti, bukan tinjauan formal yang tak akan pernah Anda jalankan.

**Bisnis kecil.** Anda mungkin tidak punya spesialis data dan membeli analitik di dalam perkakas yang sudah Anda pakai, jadi risikonya memercayai dasbor vendor tanpa mempertanyakan bagaimana metrik didefinisikan atau apakah perbandingannya adil. Habiskan perhatian langka Anda pada penalaran daripada perkakas: pisahkan korelasi dari kausalitas pada satu atau dua keputusan yang benar-benar menggerakkan bisnis, dan nyatakan rentang jujur kepada diri sendiri sebelum berkomitmen uang yang tak dapat kembali. Ketika perkakas menawarkan mengotomatisasi keputusan, jaga orang dalam lingkaran di mana pun panggilan salah akan merugikan pelanggan.

**Enterprise.** Lintas banyak tim masalahnya konsistensi dan tata kelola: ekspektasi bersama bahwa analisis menamai keputusan dan kriteria hentikan di muka, bahwa klaim kausal menyatakan asumsinya, dan bahwa angka berdampak membawa rentang ke paket dewan dan audit. Pisahkan metrik pembelajaran dari evaluasi kinerja di seluruh organisasi agar pengukuran tidak membusuk menjadi pengawasan dan manipulasi. Berinvestasilah pada literasi data luas dan pada praktik tinjauan seperti advokat iblis dan pra-registrasi, agar pemaparan percaya diri tak dapat menggantikan bukti pada skala besar.

**Pemerintah.** Pengadaan, transparansi, dan akuntabilitas publik menaikkan taruhan pada setiap klaim kausal, karena kebijakan yang dibenarkan korelasi palsu salah mengalokasikan uang publik dan dapat merugikan warga. Pilih desain perbandingan yang ketat untuk evaluasi program, komunikasikan efek sebagai rentang dengan asumsi dinyatakan kepada badan pengawas, dan dokumentasikan penalaran agar audit dapat mengikutinya. Arahkan pengukuran pada hasil program alih-alih mengawasi petugas kasus, dan beri publik penjelasan jelas tentang bagaimana bukti membentuk keputusan.

## Contoh

**Startup.** Startup pra-Seri-A memperhatikan bahwa pengguna yang bergabung dengan forum komunitasnya churn jauh lebih sedikit, dan para pendiri siap mengarahkan seluruh peta jalan ke fitur forum. Sebelum berkomitmen, salah satunya bertanya apa yang akan mengubah pikiran mereka, dan tinjauan cepat menunjukkan bahwa pelanggan yang sudah berkomitmen hanyalah mereka yang repot bergabung dengan forum. Mereka menjalankan eksperimen kecil alih-alih mempertaruhkan kuartal pada korelasi, dan menjadikan "apa yang akan mengubah pikiran kita?" pertanyaan standar dalam dokumen keputusan mereka.

**Enterprise.** Sebuah perusahaan jasa keuangan memperhatikan bahwa pelanggan yang memakai fitur tertentu memiliki churn jauh lebih rendah dan nyaris meluncurkan kampanye mahal untuk mendorong semua orang ke fitur itu. Tinjauan ilmu keputusan menandai confounder yang jelas: pelanggan yang sudah terlibat memilih sendiri masuk ke fitur. Eksperimen terkendali kemudian menunjukkan fitur itu sendiri berefek kausal kecil pada churn. Perusahaan menghindari investasi besar yang salah arah, dan pimpinan mengadopsi "apa yang akan mengubah pikiran kita?" sebagai pertanyaan standar sebelum pengeluaran besar.

**Pemerintah.** Sebuah lembaga publik yang mengevaluasi program ketenagakerjaan menahan diri dari mengklaim keberhasilan dari statistik mentah bahwa peserta menemukan kerja dengan laju tinggi, menyadari bahwa orang bermotivasi memilih sendiri masuk ke program semacam itu. Ia memakai desain perbandingan ketat dan mengomunikasikan efek terestimasi sebagai rentang dengan asumsi dinyatakan kepada badan pengawas. Pengukuran berfokus pada hasil program alih-alih mengawasi petugas kasus, yang menjaga kepercayaan garis depan sambil tetap mendorong akuntabilitas dan perbaikan.

## Kasus bisnis: motivasi, ROI, dan TCO

ROI ilmu keputusan adalah biaya yang dihindari dari keputusan salah yang yakin dan kualitas keputusan yang lebih baik yang dibuat organisasi ribuan kali. Satu pilihan strategis atau kebijakan besar yang dibenarkan korelasi palsu dapat memboroskan jauh lebih banyak daripada seluruh biaya membangun praktik keputusan yang baik. Kalibrasi lebih baik (mengetahui apa yang Anda ketahui dan tidak ketahui) memungkinkan Anda menakar taruhan dengan tepat dan menghindari komitmen sembrono maupun kelumpuhan. Secara agregat, budaya berbasis data bertambah berbunga: setiap tim membuat keputusan yang sedikit lebih baik dan lebih tertalar adalah daya ungkit yang sangat besar.

Biaya adopsi sebagian besar budaya dan pendidikan: pelatihan literasi data, waktu untuk analisis dan tinjauan cermat, dan kesediaan pimpinan mengubah keputusan serta mengakui ketidakpastian. Dalam dolar ia lebih murah daripada platform bab-bab sebelumnya tetapi lebih sulit dipasang, karena ia meminta orang berkuasa untuk diatur oleh bukti. Timbang terhadap biaya tidak mengadopsi: sandiwara data yang memboroskan upaya analitis, keputusan digerakkan suara paling percaya diri, klaim kausal yang runtuh saat bersentuhan dengan kenyataan, dan, di mana pengawasan berakar, tenaga kerja yang memanipulasi metrik dan menyembunyikan kabar buruk. Kepada pimpinan, kasusnya sederhana. Semua investasi data sebelumnya hanya terbayar jika mil terakhir dari wawasan ke keputusan sehat, dan ilmu keputusan adalah mil terakhir itu.

## Anti-pola dan jebakan

- Sandiwara data: analisis dibuat untuk membenarkan keputusan yang sudah dibuat.
- Meluncur dari "berkorelasi dengan" ke "menyebabkan" tanpa menginterogasi confounder.
- Menyajikan estimasi titik sebagai kepastian, menyembunyikan rentang ketidakpastian.
- Bias konfirmasi: hanya mencari data yang mendukung kesimpulan yang disukai.
- Keputusan HiPPO di mana opini orang berpenghasilan tertinggi menimpa bukti.
- Mengubah metrik menjadi pengawasan individu, memancing manipulasi dan ketakutan.
- Hukum Goodhart beraksi: metrik target yang berhenti mengukur apa yang penting.
- Menghukum orang atas kegagalan informatif, membunuh kejujuran dan eksperimen.

## Model kematangan

1. **Memulai.** Keputusan berjalan atas hierarki dan intuisi, dan suara paling keras atau paling senior menang. Korelasi bebas diperlakukan sebagai kausalitas, ketidakpastian diabaikan, dan sedikit metrik yang dipakai mengawasi individu dan dimanipulasi.
2. **Mengembangkan.** Sebagian tim berkonsultasi dengan data dan menunjukkan kesadaran akan jebakan kausal, tetapi analisis sering selektif, dibuat untuk membenarkan keputusan yang sudah dibuat. Ketidakpastian jarang dikomunikasikan, dan praktik pengukuran tidak konsisten dari tim ke tim.
3. **Membakukan.** Organisasi mendokumentasikan dan menegakkan praktik bersama: analisis diikat pada keputusan bernama dengan kriteria terdefinisi di muka, tim membedakan korelasi dari kausalitas dan memilih eksperimen untuk klaim kausal, angka membawa rentang dan asumsi dinyatakan, dan pengukuran diarahkan pada hasil alih-alih individu, dengan keamanan psikologis dilindungi.
4. **Mengelola.** Kualitas keputusan diukur dan dikendalikan terhadap garis dasar. Organisasi melacak seberapa sering analisis menamai sinyal hentikan sebelum data tiba, pangsa angka berdampak yang dikirim dengan rentang terkomunikasi, berapa klaim kausal bertumpu pada eksperimen versus korelasi telanjang, dan apakah keputusan dibalik atas bukti. Praktik penjaga bias seperti pra-registrasi dan tinjauan advokat iblis diaudit, dan metrik yang mulai dimanipulasi tertangkap dan dipensiunkan.
5. **Mengorkestrasi.** Penalaran sehat terus diperbaiki dan terintegrasi di seluruh organisasi. "Apa yang akan mengubah pikiran kita?" rutin sebelum keputusan besar mana pun, ketelitian kausal dan ketidakpastian jujur adalah norma budaya, dan pemimpin terlihat memperbarui berdasarkan bukti dan mengakui apa yang tak diketahui. Pengukuran mendorong pembelajaran tanpa pengawasan, praktik keputusan beradaptasi seiring organisasi dan risikonya bergeser, dan setiap tingkat memutuskan lebih baik sebagai hasilnya.

## Gagasan untuk didiskusikan

- Di mana dalam organisasi Anda data dipakai untuk menghiasi keputusan yang sudah dibuat?
- Keputusan terbaru mana yang bertumpu pada korelasi yang mungkin bukan kausal?
- Seberapa jujur laporan Anda mengomunikasikan ketidakpastian, dan siapa yang menolak rentang?
- Apakah metrik Anda diarahkan untuk memperbaiki sistem atau memantau individu?
- Kapan terakhir seorang pemimpin terlihat mengubah keputusan karena data?
- Bagaimana Anda menjaga pengejaran pengukuran agar tidak berjungkit menjadi pengawasan?

## Poin-poin utama

- Tujuan data adalah keputusan lebih baik; jaga dari sandiwara data.
- Nyatakan apa yang akan mengubah pikiran Anda sebelum melihat data.
- Jangan pernah mengira korelasi sebagai kausalitas; interogasi confounder dan pilih eksperimen.
- Komunikasikan ketidakpastian dengan jujur; presisi palsu menghancurkan kepercayaan ketika gagal.
- Jadilah berbasis data, bukan diperbudak data; penilaian dan konteks tetap penting.
- Ukur sistem dan hasil untuk belajar, bukan individu untuk diawasi.
- Lindungi keamanan psikologis agar orang memperbarui keyakinan dan mengungkap kabar buruk.

## Referensi dan bacaan lanjutan

- Daniel Kahneman, "Thinking, Fast and Slow."
- Judea Pearl dan Dana Mackenzie, "The Book of Why."
- Douglas W. Hubbard, "How to Measure Anything."
- Nate Silver, "The Signal and the Noise."
- Cathy O'Neil, "Weapons of Maths Destruction."
- Darrell Huff, "How to Lie with Statistics."
- Philip Tetlock dan Dan Gardner, "Superforecasting."
- Charles Wheelan, "Naked Statistics."
