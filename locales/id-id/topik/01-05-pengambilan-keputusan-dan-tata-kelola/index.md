# 1.5 Pengambilan keputusan dan tata kelola

## Tinjauan dan motivasi

Setiap sistem perangkat lunak adalah jumlah dari ribuan keputusan: [basis data](https://en.wikipedia.org/wiki/Database) mana, arsitektur mana, pustaka mana, membangun atau membeli, kapan berutang dan kapan melunasinya. Tata kelola adalah cara Anda membuat keputusan-keputusan ini dengan baik dan konsisten, melibatkan orang yang tepat tanpa menciptakan hambatan, dan menjaga alasannya agar tim masa depan tidak ditakdirkan mempelajarinya lagi dari awal. Dalam tim kecil, keputusan terjadi dalam percakapan dan hidup dalam ingatan bersama. Pada skala besar, ingatan itu menguap. Orang pergi, tim direorganisasi, dan "mengapa" di balik pilihan penting hilang, membuat penerus menirunya secara membabi buta atau mencabutnya tanpa pikir. Tata kelola yang baik adalah mesin yang membuat keputusan terlihat, disengaja, dan tahan lama di seluruh organisasi yang besar dan terus berubah.

Tantangan utama bagi tim besar adalah menyeimbangkan otonomi dengan keselarasan. Dorong semua keputusan ke atas ke dewan pusat, dan Anda mendapat konsistensi, tetapi dengan biaya hambatan yang melumpuhkan dan tim yang tak berdaya. Dorong semua keputusan ke bawah, dan Anda mendapat kecepatan, tetapi dengan biaya kekacauan: teknologi yang tidak kompatibel, upaya ganda, dan kesalahan yang berulang. Jawaban yang matang bukan sentralisasi maupun anarki. Jawabannya adalah model berlapis. Tim memutuskan sebagian besar hal secara lokal dalam "jalan beraspal" yang ditandai dengan baik, sementara proses ringan yang transparan mengatur pilihan lintas bidang yang benar-benar sulit dibalik. Tujuannya adalah menjadikan keputusan baik sebagai bawaan yang mudah, dan membelanjakan perhatian tata kelola yang langka hanya di tempat yang benar-benar penting.

Enterprise dan pemerintah memikul taruhan yang lebih tinggi. Mereka harus memuaskan auditor, regulator, dan badan pengawas yang menuntut keputusan terdokumentasi dan dapat dipertanggungjawabkan. Mereka bekerja pada horizon waktu panjang, di mana pilihan arsitektur yang buruk atau timbunan [utang teknis](https://en.wikipedia.org/wiki/Technical_debt) yang tak dikelola dapat membebani mereka selama satu dekade. Dan kewajiban pengadaan serta kepatuhan mereka membuat keputusan membangun-atau-membeli sangat berdampak dan sulit dibalik. Bagi organisasi-organisasi ini, pengambilan keputusan yang disiplin dan tercatat dengan baik bukanlah birokrasi demi birokrasi. Ia adalah manajemen risiko, memori institusional, dan fondasi akuntabilitas.

## Prinsip utama

- Catat keputusan beserta alasannya; keputusan tanpa alasan adalah liabilitas.
- Dorong keputusan ke tingkat terendah yang memiliki konteks, dalam pagar pembatas yang jelas.
- Sesuaikan bobot proses dengan bobot dan keterbalikan keputusan.
- Bedakan keputusan yang dapat dibalik ("pintu dua arah") dari yang tidak dapat dibalik ("pintu satu arah") dan atur secara berbeda.
- Pilih jalan beraspal dan bawaan daripada persetujuan kasus per kasus.
- Perlakukan utang teknis sebagai portofolio yang dikelola, bukan kegagalan moral yang disembunyikan.
- Buat tata kelola transparan; pengambilan keputusan tersembunyi menumbuhkan ketidakpercayaan dan pengerjaan ulang.

## Rekomendasi

### Adopsi Architecture Decision Record dan proses RFC yang disesuaikan ukurannya

[Architecture Decision Record](https://en.wikipedia.org/wiki/Architectural_decision) (ADR) adalah dokumen singkat yang tak berubah yang menangkap satu keputusan penting: konteksnya, opsi yang dipertimbangkan, pilihan yang diambil, dan konsekuensinya. Simpan ADR di kontrol versi bersama kode, sehingga alasannya berjalan bersama sistem. Untuk keputusan yang membutuhkan masukan sebelum dibuat, gunakan proses [RFC](https://en.wikipedia.org/wiki/Request_for_Comments) (request for comments) yang ringan: edarkan usulan, undang komentar dalam jangka terbatas, lalu putuskan dan catat. Jaga keduanya tetap ringan. Nilainya ada pada pemikiran dan catatan yang tahan lama, bukan pada templat yang rumit. Bersama-sama, ADR dan RFC mengubah alasan yang tersirat dan terlupakan menjadi memori institusional yang dapat dicari.

### Atur melalui jalan beraspal, bukan penjaga gerbang

Alih-alih meninjau setiap keputusan satu per satu, berinvestasilah pada "jalan beraspal": seperangkat bawaan yang direstui dan didukung baik, bahasa, kerangka kerja, pipeline deployment, dan pola yang disetujui, yang dapat diadopsi tim dengan sedikit gesekan dan banyak dukungan. Tim yang tetap di jalan beraspal membutuhkan sedikit tata kelola, karena pilihan yang aman dan patuh juga yang mudah. Tim dengan alasan sejati untuk meninggalkannya boleh, tetapi mereka memikul tanggung jawab tambahan dan tinjauan ringan. Model "jalur emas" ini jauh lebih skalabel daripada dewan pusat yang menyetujui segalanya, karena memindahkan tata kelola dari penjagaan gerbang kasus per kasus ke bawaan yang dirancang dengan baik.

### Gunakan dewan tinjauan arsitektur secukupnya dan secara transparan

Dewan tinjauan arsitektur, atau padanannya, memiliki peran yang sah untuk keputusan terbesar, paling lintas bidang, atau paling tidak dapat dibalik, dan untuk menetapkan standar yang mendefinisikan jalan beraspal. Jaga cakupannya sempit, kriterianya diterbitkan, dan prosesnya cepat dan bersifat saran, bukan hambatan wajib untuk pekerjaan rutin. Tugas dewan adalah mengelola koherensi dan berbagi pengetahuan, bukan menyetujui setiap pilihan. Ketika dewan menjadi antrean yang harus ditunggu setiap proyek, ia telah gagal. Delegasikan secara agresif, dan sisakan tinjauan pusat untuk beberapa keputusan yang benar-benar memerlukannya.

### Jadikan membangun-versus-membeli-versus-mengadopsi sebagai analisis yang disengaja

Untuk kemampuan penting apa pun, timbang tiga jalur: bangun sendiri, beli produk komersial, atau adopsi solusi [sumber terbuka](https://en.wikipedia.org/wiki/Open-source_software). Bangun bila kemampuan itu pembeda sejati dan inti misi Anda. Beli atau adopsi kemampuan tak berdiferensiasi yang dikerjakan orang lain dengan lebih baik. Hitung [total biaya kepemilikan](https://en.wikipedia.org/wiki/Total_cost_of_ownership) (TCO), bukan hanya harga di muka. Membeli menimbulkan biaya lisensi, integrasi, dan [lock-in](https://en.wikipedia.org/wiki/Vendor_lock-in). Membangun menimbulkan pemeliharaan dan penugasan staf yang abadi. Mengadopsi sumber terbuka menimbulkan kewajiban dukungan dan pelacakan keamanan. Catat keputusan dan asumsinya sebagai ADR, agar Anda dapat meninjaunya kembali ketika keadaan berubah.

### Kelola utang teknis sebagai portofolio

Utang teknis tidak buruk pada dasarnya. Kadang menanggungnya agar rilis lebih cepat adalah keputusan yang benar. Yang buruk adalah utang yang tak terkelola, tak terlihat, dan terlupakan. Simpan inventaris eksplisit utang yang signifikan. Untuk setiap butir, catat biaya yang ditimbulkannya ("bunga" berkelanjutan) dan biaya memperbaikinya. Lalu kelola seperti portofolio keuangan. Lunasi utang berbunga tinggi yang memperlambat tim setiap hari. Toleransi utang berbunga rendah di sudut-sudut yang stabil. Buat keputusan utang secara sadar, bukan kebetulan. Sisihkan sebagian tetap dari kapasitas untuk melunasi utang, agar tidak pernah berlipat menjadi krisis.

### Bedakan keputusan yang dapat dibalik dari yang tidak dapat dibalik

Tidak semua keputusan layak dipertimbangkan sama. Keputusan "pintu dua arah" yang dapat dibalik mudah dibatalkan, jadi buatlah dengan cepat dan lokal, oleh tim, dengan kecenderungan bertindak. Menyiksa diri atasnya membuang waktu dan memperlambat pembelajaran. Keputusan "pintu satu arah" yang tidak dapat dibalik atau mahal dibalik, kontrak [API](https://en.wikipedia.org/wiki/API) publik, model data berskala besar, komitmen vendor multitahun, layak mendapat pertimbangan yang lambat, cermat, dan senior serta alasan yang tercatat. Mengklasifikasi keputusan dengan cara ini adalah salah satu kebiasaan tata kelola dengan daya ungkit tertinggi yang Anda miliki. Ia mengarahkan pengawasan yang langka ke tempat yang berbuah, dan membuka hambatan untuk segala hal lain.

## Trade-off: kelebihan dan kekurangan

| Pendekatan tata kelola | Kelebihan | Kekurangan |
| --- | --- | --- |
| Dewan tinjauan pusat untuk semua | Konsistensi dan pengawasan maksimum | Hambatan parah; melemahkan tim; lambat |
| Jalan beraspal dengan otonomi lokal | Skalabel, cepat, bawaan aman, memberdayakan tim | Perlu investasi platform di muka; sebagian menyimpang dari jalan |
| Otonomi tim penuh, tanpa tata kelola | Cepat, kepemilikan tinggi | Fragmentasi, duplikasi, kesalahan berulang |
| ADR / RFC | Memori tahan lama, keputusan lebih baik, transparansi | Beban menulis; diabaikan jika tidak dipelihara |

| Pilihan sumber | Kelebihan | Kekurangan |
| --- | --- | --- |
| Bangun | Kendali penuh, pas persis, dapat membedakan | Biaya pemeliharaan dan staf yang abadi |
| Beli | Cepat, didukung, orang lain yang memelihara | Biaya lisensi, lock-in, kecocokan tidak sempurna |
| Adopsi (sumber terbuka) | Tanpa biaya lisensi, dapat diperiksa, komunitas | Beban dukungan dan keamanan jatuh pada Anda |

Trade-off yang menyatukan adalah kendali versus kecepatan, dan konsistensi pusat versus otonomi lokal. Setiap pilihan tata kelola berada pada spektrum ini. Sikap yang direkomendasikan, jalan beraspal ditambah delegasi berbasis keterbalikan, dengan sengaja membeli sebagian besar kecepatan otonomi sambil mempertahankan konsistensi yang penting. Ia melakukannya dengan menjadikan pilihan yang selaras sebagai yang mudah, dan menyisakan proses berat untuk keputusan tak terbalikkan yang jarang.

## Pertanyaan untuk didiskusikan dengan tim Anda

1. **Siapa yang memutuskan apakah suatu keputusan adalah pintu satu arah, dan bagaimana Anda akan menangkap salah klasifikasi ke kedua arah?** Mengklasifikasi keputusan berdasarkan keterbalikan adalah salah satu kebiasaan tata kelola dengan daya ungkit tertinggi, dan nilainya runtuh jika Anda salah melabeli: perlakukan pilihan yang dapat dibalik sebagai tidak dapat dibalik dan Anda menenggelamkannya dalam pertimbangan, perlakukan yang tidak dapat dibalik sebagai dapat dibalik dan Anda merilis model data atau kontrak API publik yang tidak murah dibatalkan. Risiko yang bersaing adalah bahwa orang yang paling dekat dengan pekerjaan mungkin condong ke kecepatan, sementara dewan pusat mungkin condong ke kehati-hatian. Bawa contoh konkret ke diskusi: berapa sebenarnya biaya, dalam waktu dan uang, untuk membalik setiap keputusan, dan siapa yang menanggungnya. Dalam konteks enterprise dan pemerintah, komitmen pengadaan dan data berskala besar mengubah banyak pilihan menjadi pintu satu arah yang tampak dapat dibalik di awal. Sepakati siapa yang mengklasifikasi, dan bangun kebiasaan pendapat kedua yang cepat atas apa pun yang mendekati batas, agar pengawasan yang langka mendarat di tempat pembalikan benar-benar mahal.

2. **Siapa yang memiliki, mendanai, dan mengisi staf jalan beraspal, dan apa yang mencegahnya membusuk menjadi penjaga gerbang?** Jalan beraspal hanya berfungsi jika bawaan yang direstui benar-benar didukung baik dan lebih mudah daripada alternatifnya, dan itu memerlukan investasi berkelanjutan yang mudah kekurangan dana. Trade-off-nya tajam: jalan beraspal yang kekurangan sumber daya menjadi sekumpulan mandat tanpa dukungan, persis penjagaan gerbang yang hendak digantikan model ini, dan tim lalu mencari jalan memutar. Bawa bukti kesehatan jalan itu: tingkat adopsi, seberapa mutakhir perkakas yang disetujui, seberapa cepat tim platform merespons, dan seberapa sering tim mengajukan untuk keluar jalur. Bagi organisasi besar dan yang diatur regulasi, jalan beraspal juga cara pilihan yang patuh menjadi yang mudah, sehingga pendanaannya adalah investasi kepatuhan, bukan sekadar kenyamanan. Tetapkan pemilik yang jelas dan anggaran tetap, dan ukur apakah tim memilih jalan itu karena benar-benar jalur termudah.

3. **Di mana tim mencari jalan memutar dari tata kelola Anda, dan apa yang dikatakan TI bayangan itu kepada Anda?** Tim menghindari jalur yang disahkan ketika lebih menyakitkan daripada solusi akalnya, jadi TI bayangan yang meluas lebih merupakan vonis desain atas tata kelola Anda daripada masalah disiplin. Pertimbangan yang bersaing itu nyata: sebagian penghindaran ceroboh, dan banyak yang merupakan penghindaran rasional dari dewan tinjauan yang telah menjadi antrean berminggu-minggu. Bawa buktinya: persetujuan mana yang dilewati, perkakas tidak resmi mana yang diam-diam menyebar, dan berapa lama jalur resmi sebenarnya. Dalam konteks enterprise dan pemerintah taruhannya lebih tinggi, karena perkakas yang tidak disahkan dapat melanggar kewajiban audit, keamanan, dan pengadaan yang berbobot hukum. Jika polanya menunjukkan orang memutari hambatan, perbaikannya adalah mempercepat dan memperluas jalan beraspal serta mengecilkan cakupan dewan ke beberapa keputusan lintas bidang yang tak terbalikkan, bukan menambah persetujuan.

4. **Berapa banyak kapasitas pengiriman kita yang sebenarnya dipakai untuk melunasi utang teknis, dan dapatkah kita menyebut butir berbunga tertinggi yang harus ditargetkan lebih dulu?** Utang teknis berperilaku seperti bunga majemuk, pajak diam-diam atas setiap perubahan mendatang, dan organisasi besar dapat memikulnya bertahun-tahun sebelum ada yang menyadari sistem telah menjadi lambat dan rapuh untuk diubah. Tekanan yang bersaing itu blak-blakan: setiap jam yang dihabiskan untuk utang adalah jam yang tidak dihabiskan untuk fitur yang dapat dilihat pimpinan, sehingga pelunasan adalah hal pertama yang dipotong ketika tenggat mengetat. Bawa bukti nyata ke diskusi, inventaris tertulis utang signifikan, estimasi jujur biaya berkelanjutan yang ditimbulkan tiap butir dan biaya memperbaikinya, dan persentase aktual kapasitas terkini yang dipakai untuk pelunasan versus pekerjaan baru. Bagi enterprise dan badan pemerintah pada horizon waktu satu dekade, utang yang tak dikelola akhirnya memaksa penulisan ulang yang mahal atau temuan audit, jadi perlakukan alokasi pelunasan tetap sebagai manajemen risiko dan putuskan siapa yang menjaganya ketika jadwal meleset.

5. **Ketika kita membutuhkan alasan di balik keputusan yang dibuat dua tahun lalu, dapatkah kita benar-benar menemukannya, dan adakah yang menjaga catatan itu tetap hidup?** Seluruh nilai Architecture Decision Record adalah bahwa alasan hidup lebih lama daripada orang yang membuatnya, dan nilai itu runtuh jika ADR ditulis sekali, tidak pernah dicari, dan diam-diam menjadi usang. Ketegangannya ada antara disiplin menulis yang diperlukan untuk menangkap konteks, opsi, dan konsekuensi pada saat keputusan, dan tekanan harian untuk langsung merilis dan melanjutkan. Bawa uji konkret ke diskusi: pilih tiga keputusan penting terbaru dan lihat apakah ada yang dapat menemukan alasan tercatatnya dalam hitungan menit, dan periksa apakah ADR yang digantikan ditandai demikian alih-alih diam-diam bertentangan dengan praktik saat ini. Dalam konteks enterprise dan pemerintah, catatan yang dapat dicari itu persis bukti yang dapat dipertanggungjawabkan yang dituntut auditor dan badan pengawas, jadi putuskan di mana ADR disimpan, siapa yang meninjaunya, dan apa yang membuat keputusan cukup penting untuk dicatat.

6. **Kapan terakhir kali kita membuka kembali keputusan besar membangun-versus-membeli terhadap asumsi aslinya, dan apakah kita akan menyadari ketika asumsi itu kedaluwarsa?** Pilihan sumber adalah di antara keputusan paling mahal dan sulit dibalik yang Anda buat, dan asumsi di baliknya (harga vendor, staf Anda sendiri, kematangan opsi sumber terbuka) diam-diam menjadi basi sementara keputusan tetap membeku di tempat. Pertimbangan yang bersaing menimbang biaya hangus dan gangguan beralih terhadap biaya lock-in yang menumpuk, kecocokan yang tidak sempurna, atau beban pemeliharaan yang tidak lagi Anda inginkan. Bawa ADR asli dan asumsi yang dinyatakannya, estimasi total biaya kepemilikan terkini untuk setiap jalur termasuk lisensi, integrasi, staf, dan biaya keluar, dan sinyal apa pun, perubahan harga atau penurunan dukungan, bahwa suatu premis telah bergeser. Bagi pembeli pemerintah dan yang diatur regulasi, aturan pengadaan dan kontrak multitahun membuat pintu satu arah ini sangat mengikat, jadi sepakati sebelumnya pemicu dan irama yang akan memaksa keputusan ulang yang disengaja alih-alih perpanjangan buta.

## Lensa sektor

**Startup.** Atur hampir tidak ada dan bersandarlah kuat pada kecepatan: untuk pilihan pintu dua arah yang dapat dibalik, putuskan di meja dan lanjutkan. Sisakan satu kebiasaan tata kelola Anda untuk segelintir pintu satu arah, model data inti atau vendor fundamental, dan tangkap masing-masing dalam satu paragraf agar rekan di masa depan tidak mengadilinya lagi dari awal. Lewati dewan tinjauan dan jalan beraspal sepenuhnya, karena pada ukuran Anda itu beban yang tidak sanggup Anda tanggung dan seluruh tim sudah berbagi konteks.

**Bisnis kecil.** Tanpa arsitek di staf, jadikan membangun-versus-membeli pertanyaan tata kelola utama Anda dan jawab berdasarkan total biaya kepemilikan, bukan preferensi. Pilih bawaan membeli atau mengadopsi perkakas yang didukung baik untuk apa pun yang bukan pembeda inti Anda, karena pemeliharaan abadi adalah biaya yang paling tidak sanggup Anda pikul. Simpan satu log keputusan ringan agar alasan di balik beberapa pilihan penting Anda bertahan ketika orang kunci pergi.

**Enterprise.** Masalah Anda adalah menyeimbangkan otonomi dengan keselarasan di banyak tim, jadi berinvestasilah pada jalan beraspal yang didanai dan sisakan dewan tinjauan arsitektur yang sempit dan cepat untuk keputusan lintas bidang dan tak terbalikkan yang sejati. Bakukan ADR agar alasan menjadi memori institusional yang dapat dicari, dan kelola utang teknis dan pilihan sumber sebagai portofolio dengan anggaran tetap. Ukur apakah tim memilih jalan itu karena yang termudah, dan kecilkan dewan mana pun yang telah membusuk menjadi antrean.

**Pemerintah.** Keputusan yang terdokumentasi dan dapat dipertanggungjawabkan bukan pilihan di sini: auditor dan badan pengawas mengharapkan melihat alasan, opsi yang ditimbang, dan asumsi di balik setiap pilihan penting. Jalankan membangun-versus-membeli sebagai analisis total biaya kepemilikan yang tercatat, hormati aturan pengadaan yang membatasi lock-in sumber tunggal, dan simpan ADR sebagai jejak bukti siap-audit. Anggap serius horizon waktu panjang, karena model data atau komitmen vendor yang dibuat hari ini dapat mengikat organisasi selama satu dekade, jadi klasifikasikan sebagai pintu satu arah dan pertimbangkan dengan semestinya.

## Contoh

**Startup.** Sebuah startup empat orang membuat sebagian besar keputusan dalam hitungan menit di meja bersama, dan untuk pilihan pintu dua arah yang dapat dibalik kecepatan itu keuntungan nyata, jadi mereka menolak beban tata kelola apa pun. Tetapi ketika mereka memilih basis data dan model data yang akan menyakitkan diubah kelak (pintu satu arah), mereka berhenti untuk menulis catatan satu paragraf: opsi, pilihan, dan asumsi di baliknya. Setahun kemudian, ketika menabrak batas penskalaan, satu catatan itu menyelamatkan mereka dari mengadili ulang pertanyaan dari awal. Mereka mengatur hampir tidak ada, dan menyisakan satu kebiasaan ringan mereka untuk beberapa keputusan yang benar-benar mahal dibalik.

**Enterprise.** Tim platform sebuah enterprise besar lumpuh oleh dewan tinjauan arsitektur yang harus menyetujui setiap pilihan teknologi, menciptakan antrean berminggu-minggu. Enterprise menata ulang tata kelola di sekitar jalan beraspal: katalog terkurasi bahasa, penyimpanan data, dan pipeline yang disetujui dan didukung penuh yang dapat langsung diadopsi tim. ADR mencatat keputusan apa pun untuk menyimpang, dan tinjauan cepat yang bersifat saran hanya menangani pilihan di luar jalur. Cakupan dewan menyusut ke penetapan standar dan segelintir keputusan lintas bidang yang sejati. Pengiriman melesat tajam. Konsistensi justru membaik, karena jalur mudah kini adalah jalur yang patuh. Dan arsip ADR memberi organisasi catatan yang dapat dicari tentang mengapa segala sesuatu dibangun seperti adanya.

**Pemerintah.** Sebuah departemen pemerintah menghadapi keputusan besar membangun-versus-membeli untuk platform manajemen kasus di bawah aturan pengadaan dan audit yang ketat. Alih-alih memutuskan berdasarkan preferensi, departemen menjalankan analisis total biaya kepemilikan terdokumentasi atas tiga opsi: membangun kustom, membeli produk komersial, dan mengadopsi basis sumber terbuka. Ia menimbang lisensi, integrasi, pemeliharaan jangka panjang, staf, dan lock-in, dan mencatat keputusan serta asumsinya sebagai ADR. Bertahun-tahun kemudian, ketika syarat vendor berubah, departemen meninjau kembali ADR itu, menemukan asumsi aslinya tidak lagi berlaku, dan memutuskan ulang dengan pengetahuan penuh tentang alasan sebelumnya, menghindari migrasi buta yang mahal. Alasan yang tercatat itu juga persis bukti yang dapat dipertanggungjawabkan yang dibutuhkan auditor.

## Kasus bisnis: motivasi, ROI, dan TCO

Keputusan adalah biaya berdaya ungkit tertinggi dan paling tak terlihat dalam perangkat lunak. Satu pilihan arsitektur atau sumber yang buruk dan tak terbalikkan dapat menimbulkan hambatan bertahun-tahun atau perbaikan sembilan digit. Mengaturnya dengan baik, beberapa jam pertimbangan dan catatan tertulis, hampir tidak memakan biaya jika dibandingkan. Imbal hasil ADR dan delegasi berbasis keterbalikan berasal dari dua sumber: menghindari kesalahan mahal pada keputusan pintu satu arah, dan menghindari pertimbangan sia-sia serta pengerjaan ulang pada segala hal lain. Alasan yang tercatat juga memangkas biaya berulang mengadili ulang pertanyaan yang sudah diselesaikan dan tim merekayasa balik maksud di balik sistem warisan.

Utang teknis membuat argumen TCO menjadi konkret. Utang yang tak dikelola berperilaku persis seperti bunga majemuk: pajak yang tumbuh atas setiap perubahan mendatang, sampai sistem menjadi pada dasarnya tidak dapat dipelihara dan menuntut penulisan ulang yang mahal. Mengelola utang sebagai portofolio, dengan alokasi kapasitas tetap untuk melunasi butir berbunga tinggi, jauh lebih murah daripada krisis yang akhirnya datang. Tata kelola yang baik murah diadopsi, sebagian besar disiplin menuliskan keputusan dan investasi awal pada jalan beraspal. Melewatkannya mahal: Anda membayar dalam penulisan ulang yang dapat dihindari, kejutan lock-in, kegagalan audit, dan hilangnya memori institusional. Untuk meyakinkan pimpinan, bingkai tata kelola dalam bahasa mereka: pengurangan risiko, pengerjaan ulang yang dihindari, pengiriman lebih cepat lewat jalan beraspal, dan ketahanan siap-audit. Tunjukkan bahwa tujuannya bukan lebih banyak proses tetapi proses yang lebih tepat sasaran, pengawasan berat hanya di tempat pembalikan mahal, dan kecepatan tanpa gesekan di tempat lain.

## Anti-pola dan jebakan

- Keputusan tak terdokumentasi: alasan hilang begitu orang yang membuatnya pergi.
- Hambatan dewan persetujuan: badan pusat yang harus diantrekan setiap proyek.
- Proses satu ukuran: memaksa keputusan sepele yang dapat dibalik melalui tinjauan berat.
- Kelumpuhan analisis: menyiksa diri atas keputusan pintu dua arah yang mudah dibalik.
- [TI bayangan](https://en.wikipedia.org/wiki/Shadow_IT): tim menghindari tata kelola sepenuhnya karena jalur yang disahkan terlalu menyakitkan.
- Utang teknis tak terlihat: utang yang tidak pernah diinventarisasi, tidak pernah dilunasi, diam-diam berlipat.
- Refleks bangun-semua atau beli-semua: memilih sumber berdasarkan kebiasaan, bukan analisis TCO.
- Sandiwara tata kelola: dokumen dan dewan yang ada demi penampilan tetapi tidak membentuk keputusan.

## Model kematangan

- Tingkat 1 (Memulai): Keputusan bersifat ad hoc dan tak tercatat; tata kelola tidak ada atau berupa hambatan menyeluruh; utang teknis tak terlihat dan alasan di balik pilihan menguap ketika orang pergi.
- Tingkat 2 (Mengembangkan): Beberapa keputusan didokumentasikan dan ada sebagian tinjauan, tetapi praktiknya tidak konsisten antartim dan prosesnya sering tidak sesuai dengan bobot dan keterbalikan keputusan.
- Tingkat 3 (Membakukan): ADR, jalan beraspal, delegasi berbasis keterbalikan, dan inventaris utang didokumentasikan dan ditegakkan di seluruh organisasi, sehingga pilihan yang patuh adalah bawaan yang mudah dan alasan dapat dicari.
- Tingkat 4 (Mengelola): Tata kelola diukur terhadap garis dasar: adopsi jalan beraspal, cakupan ADR, waktu siklus keputusan, utang sebagai persentase kapasitas, dan tingkat pengecualian di luar jalur dilacak, dan keputusan melunasi utang atau meninjau ulang sumber dipicu oleh bukti itu, bukan krisis.
- Tingkat 5 (Mengorkestrasi): Tata kelola terus disetel dan terintegrasi dengan perencanaan pengiriman dan risiko; pengawasan diarahkan tepat pada keputusan tak terbalikkan; utang dan pilihan sumber diseimbangkan ulang secara aktif sebagai portofolio dan diputuskan ulang berdasarkan bukti seiring bergesernya keadaan.

## Gagasan untuk didiskusikan

- Untuk keputusan terpenting kita yang terbaru, dapatkah kita menemukan alasan tercatat di baliknya?
- Di mana tata kelola kita menjadi hambatan, dan di mana ia tidak ada padahal dibutuhkan?
- Keputusan kita saat ini yang mana yang merupakan pintu satu arah, dan apakah kita memperlakukannya demikian?
- Berapa banyak kapasitas kita yang dipakai untuk melunasi utang teknis, dan apakah cukup?
- Apakah tim kita mengikuti jalan beraspal karena benar-benar jalur termudah, atau memutarinya?
- Kapan terakhir kali kita meninjau kembali keputusan besar membangun-versus-membeli terhadap asumsi aslinya?

## Poin-poin utama

- Catat keputusan penting dan alasannya dengan ADR; buat alasan tahan lama.
- Atur melalui jalan beraspal dan bawaan, bukan penjagaan gerbang kasus per kasus.
- Sesuaikan bobot proses dengan bobot dan keterbalikan keputusan; delegasikan pintu dua arah, pertimbangkan pintu satu arah.
- Analisis membangun-versus-membeli-versus-mengadopsi berdasarkan total biaya kepemilikan, dan catat asumsinya.
- Kelola utang teknis sebagai portofolio eksplisit dengan alokasi pelunasan tetap.
- Jaga tata kelola transparan dan ringan; arahkan pengawasan yang langka ke tempat pembalikan mahal.

## Referensi dan bacaan lanjutan

- Michael Nygard, "Documenting Architecture Decisions" (pola ADR asli)
- Gregor Hohpe, "The Software Architect Elevator" dan "37 Things One Architect Knows"
- Surat pemegang saham Amazon tentang keputusan Type 1 vs Type 2 (pintu satu arah vs dua arah)
- Ward Cunningham, metafora asli "utang teknis"
- Martin Fowler, tulisan tentang utang teknis dan arsitektur evolusioner
- Neal Ford, Rebecca Parsons, Patrick Kua, "Building Evolutionary Architectures"
- Nicole Forsgren, Jez Humble, Gene Kim, "Accelerate" (arsitektur berpasangan longgar dan otonomi)
- ISO/IEC/IEEE 42010 tentang deskripsi arsitektur
