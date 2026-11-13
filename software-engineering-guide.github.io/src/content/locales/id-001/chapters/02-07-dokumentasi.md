# 2.7 Dokumentasi

## Tinjauan dan motivasi

[Dokumentasi](https://en.wikipedia.org/wiki/Software_documentation) adalah pengetahuan tertulis yang memungkinkan orang menggunakan, mengoperasikan, dan mengubah perangkat lunak tanpa harus menyusun pemahaman dari kode saja. Ia hadir dalam banyak genre: cara memulai, cara menyelesaikan suatu tugas, bagaimana sistem distrukturkan, bagaimana menanggapi insiden, apa yang diterima dan dikembalikan sebuah [API](https://en.wikipedia.org/wiki/API). Masing-masing melayani pembaca berbeda dengan kebutuhan berbeda. Dokumentasi yang baik bukan opsional. Ia adalah beda antara pengetahuan yang berskala di organisasi besar dan pengetahuan yang hidup di kepala segelintir orang.

Bagi tim besar, dokumentasi adalah pertahanan terbaik Anda terhadap risiko orang kunci (bahaya ketika pengetahuan kritis berada pada satu atau beberapa orang saja) dan cara tercepat mengorientasi pendatang baru. Ketika ratusan insinyur bergantung pada sistem yang tidak mereka bangun, dan orang bergabung, berpindah, serta pergi sepanjang waktu, organisasi hanya dapat berfungsi bila pengetahuan dituliskan dan mudah ditemukan. Sistem tak terdokumentasi menjadi rapuh: hanya penulisnya yang dapat mengubahnya dengan aman, dan ketika mereka pergi, organisasi kehilangan kemampuan memelihara perangkat lunaknya sendiri. Itu salah satu kegagalan paling umum dan mahal pada skala besar.

Konteks enterprise dan pemerintah menaikkan taruhan lebih jauh. Sistem hidup lama, jadi dokumentasi Anda harus melayani pemelihara bertahun-tahun, bahkan puluhan tahun, setelah tim asli pergi. Rezim regulasi dan audit sering mewajibkan dokumen tertentu sebagai bukti kendali: catatan arsitektur, [runbook](https://en.wikipedia.org/wiki/Runbook) (prosedur operasional dan respons insiden langkah demi langkah), dan log keputusan. Sistem sektor publik yang berpindah antarvendor bergantung sepenuhnya pada dokumentasi untuk membawa pengetahuan melintasi batas kontrak. Namun dokumentasi terkenal mudah membusuk, jadi tantangan sebenarnya adalah menjaganya akurat seiring perangkat lunak berubah.

## Prinsip utama

- Tulis untuk pembaca tertentu dengan kebutuhan tertentu; jenis dokumentasi yang berbeda melayani tujuan berbeda.
- Simpan dokumentasi dekat dengan kode dan perlakukan sebagai kode (docs-as-code).
- Akurasi mengalahkan kelengkapan; sedikit dokumentasi yang dapat dipercaya mengalahkan banyak yang keliru.
- Hasilkan apa yang dapat dihasilkan; jangan memelihara dengan tangan apa yang dapat dihasilkan perkakas dari sumber kebenaran.
- Lawan pembusukan dokumentasi secara aktif; dokumen basi lebih buruk daripada tidak ada karena menyesatkan.
- Buat dokumentasi dapat ditemukan; pengetahuan yang tak dapat ditemukan secara efektif tidak ada.
- Catat keputusan dan alasannya, bukan hanya keadaan saat ini.

## Rekomendasi

### Adopsi docs-as-code

Simpan dokumentasi di [kontrol versi](https://en.wikipedia.org/wiki/Version_control) tepat bersama kode yang dijelaskannya, tulis dalam markup teks biasa, dan tinjau lewat proses pull request yang sama. Itu menjaganya berversi, dapat ditinjau, dan dekat dengan kode, sehingga Anda dapat memperbarui keduanya bersama. Terbitkan lewat pipeline otomatis agar versi terbaru selalu tersedia. Memperlakukan dokumen sebagai kode membawa disiplin yang sama yang menjaga kode tetap tepercaya: tinjauan, riwayat, dan otomasi.

### Strukturkan konten dengan kerangka Diátaxis

Organisasikan dokumentasi ke dalam empat jenis yang berbeda, karena mencampurnya tidak melayani pembaca mana pun dengan baik: tutorial (berorientasi belajar, untuk pendatang baru), panduan cara-kerja (berorientasi tugas, untuk tujuan tertentu), rujukan (berorientasi informasi, tepat dan lengkap), dan penjelasan (berorientasi pemahaman, mengapa dan konteksnya). Pisahkan ini dan segalanya menjadi lebih mudah ditulis, dinavigasi, dan dipelihara, karena setiap halaman punya satu tugas yang jelas dan satu audiens yang jelas.

### Pelihara dokumen operasional esensial

Beri setiap repositori [README](https://en.wikipedia.org/wiki/README) yang jelas sebagai pintu depannya: apa itu, cara membangun dan menjalankannya, dan ke mana pergi berikutnya. Tulis runbook untuk tugas operasional dan respons insiden, agar siapa pun yang sedang on-call dapat bertindak, bukan hanya pakar. Simpan dokumentasi arsitektur yang menjelaskan struktur sistem dan komponen utamanya. Dan sediakan dokumentasi orientasi yang membuat insinyur baru produktif dengan cepat. Inilah dokumen yang paling Anda rindukan ketika tidak ada.

### Hasilkan dokumen API dan changelog dari sumber kebenaran

Hasilkan dokumentasi rujukan API Anda dari kontrak yang dapat dibaca mesin atau anotasi kode, agar tidak dapat menyimpang dari antarmuka sebenarnya. Simpan [changelog](https://en.wikipedia.org/wiki/Changelog), idealnya dihasilkan dari commit terstruktur atau catatan rilis, agar konsumen dapat melihat apa yang berubah antarversi. Mengotomatiskan ini mengangkat dokumentasi yang paling rawan membusuk dan dipelihara dengan tangan dari piring Anda dan menjaganya tepercaya.

### Catat keputusan arsitektur

Tangkap keputusan arsitektur dan desain yang signifikan sebagai catatan ringan bertanggal yang menyatakan konteks, keputusan, dan konsekuensinya. Catatan keputusan ini menjaga alasan yang jika tidak akan hilang, agar pemelihara mendatang dapat melihat mengapa sistem seperti adanya alih-alih meragukannya atau mengulangi kesalahan lama. Mereka sangat membuahkan hasil selama umur panjang sistem enterprise dan pemerintah.

### Lawan pembusukan dokumentasi dengan sengaja

Perlakukan dokumentasi basi sebagai cacat. Perbarui dokumen sebagai bagian dari perubahan yang sama yang mengubah perilaku, dan jadikan itu ekspektasi tinjauan. Tetapkan kepemilikan agar setiap dokumen penting punya seseorang yang bertanggung jawab. Tinjau dokumentasi bernilai tinggi untuk akurasi dari waktu ke waktu, pangkas yang usang, dan hapus atau tandai dengan jelas apa pun yang tidak lagi Anda percayai. Dokumentasi yang paling sedikit membusuk adalah dokumentasi hidup: dihasilkan atau diuji terhadap sistem itu sendiri.

### Berinvestasi pada manajemen pengetahuan dan kemudahan ditemukan

Buat dokumentasi dapat ditemukan lewat pencarian yang baik, navigasi yang jelas, dan rumah yang dikenal, agar orang dapat menemukan apa yang dibutuhkan tanpa harus bertanya kepada seseorang. Jangan biarkan terfragmentasi di terlalu banyak wiki dan perkakas yang terputus. Dan tangkap [pengetahuan tersirat](https://en.wikipedia.org/wiki/Tacit_knowledge), pemahaman informal yang hidup di utas obrolan dan kepala orang, ke bentuk yang tahan lama dan dapat ditemukan sebelum menghilang.

## Trade-off: kelebihan dan kekurangan

| Pendekatan | Kelebihan | Kekurangan |
|---|---|---|
| Docs-as-code | Berversi, dapat ditinjau, dekat dengan kode; pembusukan rendah | Memerlukan disiplin insinyur; kurang ramah bagi penulis non-teknis |
| Wiki / basis pengetahuan | Mudah disunting; dapat diakses semua orang | Menyimpang dari kode; terfragmentasi; membusuk diam-diam |
| Dokumen hasil generate (API, changelog) | Selalu akurat; pemeliharaan rendah | Terbatas pada apa yang diekspresikan sumber; perlu perkakas |
| Penjelasan tulisan tangan | Konteks dan alasan kaya yang tak dapat dihasilkan mesin | Padat karya; rawan menjadi basi |
| Struktur Diátaxis | Tujuan jelas per halaman; lebih mudah dinavigasi dan dipelihara | Upaya penstrukturan di muka; butuh disiplin penulis |

Trade-off pusatnya adalah upaya versus akurasi dan ketahanan. Dokumentasi yang paling murah ditulis, halaman wiki cepat, juga yang paling rawan membusuk dan terfragmentasi. Dokumentasi yang paling tahan lama, dihasilkan dari sumber atau ditinjau sebagai kode, memakan lebih banyak disiplin di muka tetapi tetap tepercaya. Aturan praktis yang baik: hasilkan yang bisa, simpan sisanya dekat dengan kode dan tinjau seperti kode, dan sisakan penjelasan tulisan tangan yang padat karya untuk alasan yang hanya dapat diberikan manusia.

## Pertanyaan untuk didiskusikan dengan tim Anda

1. **Apakah dokumen Anda dipisahkan menurut kebutuhan pembaca, atau tutorial, rujukan, dan penjelasan bercampur dalam satu halaman?** Bab ini merekomendasikan pemisahan Diátaxis menjadi tutorial, panduan cara-kerja, rujukan, dan penjelasan, dan menyebut pencampuran jenis sebagai anti-pola yang tidak melayani pembaca mana pun dengan baik. Pada skala besar, pendatang baru yang mempelajari sistem dan insinyur on-call yang memburu fakta presisi membutuhkan halaman berbeda, dan satu halaman campuran memperlambat keduanya. Bawa sinyalnya: pilih dokumen Anda yang paling banyak dikunjungi dan periksa apakah masing-masing punya satu tugas jelas dan satu audiens jelas. Strukturkan ulang pelanggar terburuk menjadi jenis yang berbeda, agar setiap halaman lebih mudah ditulis, dinavigasi, dan dijaga tetap mutakhir. Struktur itulah yang membuat dokumentasi dapat dipelihara seiring organisasi tumbuh.

2. **Apakah Anda menangkap keputusan arsitektur penting beserta alasannya, atau hanya keadaan saat ini?** Bab ini merekomendasikan catatan keputusan ringan bertanggal yang menyatakan konteks, keputusan, dan konsekuensi, dan mencatat bahwa mereka paling membuahkan hasil selama umur panjang sistem enterprise dan pemerintah. Tanpanya, pemelihara bertahun-tahun kemudian tidak dapat melihat mengapa sistem seperti adanya, sehingga mereka meragukan pilihan yang sehat atau mengulangi kesalahan lama. Bawa keputusan sulit terbaru yang alasannya kini hanya hidup di utas obrolan atau ingatan seseorang sebagai sinyal konkret. Adopsi format catatan keputusan singkat dan jadikan menulisnya bagian dari setiap perubahan desain penting. Alasan adalah persis pengetahuan yang hanya dapat diberikan manusia dan yang paling cepat membusuk bila tidak dituliskan.

3. **Dapatkah insinyur on-call mana pun menanggapi insiden hanya dari runbook Anda, tanpa memanggil orang yang membangun sistem?** Bab ini menyebut runbook sebagai dokumen operasional esensial agar siapa pun yang sedang on-call dapat bertindak, bukan hanya pakar, dan menggambarkan tim pemerintah yang hanya dapat mewarisi sistem karena runbook membawa pengetahuan melintasi batas kontrak. Risiko orang kunci adalah kegagalan yang dijaga terhadapnya: ketika satu pakar tak terjangkau atau pergi, prosedur pemulihan tak terdokumentasi mengubah insiden rutin menjadi pemadaman. Bawa buktinya: ambil insiden terbaru dan periksa apakah runbook saja akan menyelesaikannya. Tulis dan uji runbook untuk prosedur yang ditakuti orang, dan perlakukan runbook yang tidak dapat berdiri sendiri sebagai cacat. Itulah beda antara pemulihan pukul 2 pagi dan eskalasi pukul 2 pagi.

4. **Dokumen rujukan API dan changelog Anda yang mana yang dihasilkan dari sumber kebenaran, dan mana yang masih dipelihara dengan tangan dan diam-diam menyimpang?** Bab ini meminta Anda menghasilkan dokumentasi rujukan dari kontrak yang dapat dibaca mesin atau anotasi kode agar tidak dapat menyimpang dari antarmuka sebenarnya, dan menyebut memelihara dengan tangan konten yang dapat dihasilkan sebagai anti-pola. Bagi tim besar, dokumen API tulisan tangan yang tertinggal dari antarmuka nyata lebih buruk daripada tidak ada: setiap konsumen yang memercayainya menulis integrasi yang rusak, dan kegagalan muncul jauh dari halaman basi yang menyebabkannya. Bawa sinyal konkret: ambil segelintir antarmuka Anda yang paling banyak dipakai dan bandingkan rujukan terbitan dengan kontrak nyata untuk melihat seberapa jauh masing-masing menyimpang. Di mana Anda menemukan penyimpangan, pasang rujukan ke build agar dihasilkan ulang pada setiap perubahan, dan pensiunkan salinan yang dipelihara tangan. Dalam konteks enterprise dan pemerintah, di mana antarmuka dikonsumsi lintas tim, vendor, dan batas kontrak yang tidak pernah Anda lihat, rujukan hasil generate yang berwenang sering menjadi satu-satunya yang mencegah integrator membangun terhadap fiksi.

5. **Siapa yang memiliki setiap dokumen bernilai tinggi, dan bagaimana Anda akan mengetahui hari ini jika ada yang sudah basi?** Bab ini memperlakukan dokumentasi basi sebagai cacat dan memperingatkan bahwa dokumen tanpa pemilik membusuk karena memperbaruinya bukan tugas siapa pun, sementara dokumen basi yang disajikan sebagai mutakhir menghancurkan kepercayaan pada semua dokumentasi Anda. Pada skala besar bahayanya bukan satu halaman keliru melainkan erosi lambat kepercayaan: begitu pembaca terbakar oleh instruksi usang, mereka berhenti memercayai seluruh korpus dan kembali menginterupsi orang. Bawa peta kepemilikan dokumen paling kritis Anda dan jawaban jujur bagaimana pembusukan terdeteksi, apakah lewat irama tinjauan, generasi, tes terhadap sistem, atau murni keberuntungan. Tetapkan pemilik bernama untuk setiap dokumen yang penting, dan pilih dokumentasi hidup yang dihasilkan atau diuji agar kebasian muncul secara mekanis, bukan lewat pembaca yang malu. Untuk sistem enterprise dan pemerintah yang hidup lebih lama daripada tim aslinya, dokumentasi tanpa pemilik adalah liabilitas yang akhirnya akan ditagihkan auditor atau vendor pewaris kepada Anda.

6. **Seberapa mudah dokumentasi Anda ditemukan, dan berapa banyak pengetahuan kritis yang masih hidup hanya di utas obrolan dan kepala orang?** Bab ini mengatakan pengetahuan yang tak dapat ditemukan secara efektif tidak ada, memperingatkan agar tidak memfragmentasi dokumen di terlalu banyak wiki dan perkakas yang terputus, dan mendesak Anda menangkap pengetahuan tersirat ke bentuk yang tahan lama dan dapat ditemukan sebelum menghilang. Dalam organisasi besar fakta yang sama sering ditemukan ulang, ditanyakan ulang, dan dijawab ulang seratus kali karena tak seorang pun dapat menemukan di mana ia sudah ditulis, dan setiap kepergian membawa konteks tak tergantikan keluar pintu. Bawa buktinya: hitung berapa rumah dokumentasi terpisah yang Anda pelihara, coba temukan tiga fakta penting hanya lewat pencarian, dan catat di mana jawaban sebenarnya ternyata hidup di ingatan seseorang atau pesan yang terkubur. Konsolidasikan menuju rumah yang dikenal dengan pencarian nyata dan navigasi jelas, dan jadikan menangkap pengetahuan tersirat bagian rutin pekerjaan alih-alih penyelamatan heroik. Dalam konteks sektor publik dan yang banyak dialihdayakan, di mana sistem berpindah antarvendor dan tim lewat kontrak, pengetahuan tertulis yang dapat ditemukan adalah satu-satunya yang bertahan dari serah terima.

## Lensa sektor

**Startup.** Dengan segelintir insinyur dan tanpa runway tersisa, dokumentasikan hanya apa yang akan benar-benar dibutuhkan pemadaman pukul 2 pagi atau karyawan baru: README sejati per layanan, satu runbook teruji untuk prosedur deploy-dan-pulihkan yang ditakuti semua orang, dan beberapa catatan bertanggal tentang keputusan yang jika tidak akan Anda lupakan. Hasilkan dokumen API dari kontrak agar Anda tidak pernah memeliharanya dengan tangan. Tahan diri dari membangun platform dokumentasi; folder markup berversi di samping kode sudah cukup sampai Anda merasakan sakit yang nyata.

**Bisnis kecil.** Tanpa penulis teknis dan dengan anggaran ketat, bersandarlah pada dokumentasi yang sudah dihasilkan perkakas Anda dan pada docs-as-code ringan alih-alih program berstaf. Bingkai pilihan sebagai beli versus bangun: pilih platform yang menghasilkan rujukan mutakhir dan basis pengetahuan yang dapat dicari sendiri daripada wiki yang harus Anda rawat dengan tangan. Belanjakan upaya langka Anda pada dua atau tiga dokumen yang ketiadaannya akan menghentikan bisnis, dan biarkan halaman yang keliru atau hilang menjadi pemicu untuk memperbaiki kepemilikan.

**Enterprise.** Di banyak tim masalahnya adalah konsistensi dan kemudahan ditemukan: pipeline docs-as-code bersama, struktur umum seperti Diátaxis, rujukan API dan changelog hasil generate, dan catatan keputusan yang diterapkan sama di mana-mana agar pengetahuan tidak terfragmentasi di puluhan wiki. Tetapkan kepemilikan untuk setiap dokumen bernilai tinggi dan ukur akurasi, bukan hanya keberadaan. Perlakukan catatan arsitektur, runbook, dan log keputusan sebagai bukti audit, dan bakukan cara memproduksinya agar tinjauan kontrol menemukan jejak yang terdokumentasi dan dapat dipertanggungjawabkan, bukan kelabakan.

**Pemerintah.** Aturan pengadaan dan akuntabilitas publik menjadikan dokumentasi sebagai keluaran, bukan kesopanan. Tuliskan dokumentasi arsitektur, runbook, dan catatan keputusan ke dalam kontrak sebagai artefak wajib, ditinjau untuk akurasi agar pengetahuan bertahan dari transisi vendor dan sistem dapat dioperasikan oleh siapa pun yang mewarisinya. Wajibkan agar operator berwenang mana pun dapat menanggapi insiden hanya dari runbook, dan simpan log keputusan sebagai catatan publik yang transparan tentang mengapa pilihan dibuat. Dokumentasi tipis di sini bukan ketidaknyamanan pribadi; ia menjadi rekayasa balik mahal yang dibiayai pembayar pajak.

## Contoh

**Startup.** Sebuah startup lima orang menulis README sejati untuk setiap layanan dan runbook singkat untuk satu prosedur deploy-dan-pulihkan yang ditakuti semua orang, sehingga pemadaman pukul 2 pagi tidak bergantung pada membangunkan satu pendiri yang memahami sistem. Mereka menghasilkan dokumen API dari kontrak alih-alih menulisnya dengan tangan, dan mencatat beberapa catatan bertanggal yang menjelaskan mengapa mereka memilih basis data dan pendekatan autentikasi mereka. Tetap ringan, tetapi itu berarti karyawan keenam dan ketujuh diorientasi dari dokumen, bukan dengan menginterupsi semua orang.

**Enterprise.** Sebuah perusahaan perangkat lunak besar menyimpan semua dokumentasinya di repositori yang sama dengan kodenya, ditulis dalam markup dan ditinjau dalam pull request tepat bersama perubahan yang dijelaskannya. Rujukan API dihasilkan dari kontrak layanan, sehingga tidak pernah menyimpang. Changelog dihasilkan dari commit terstruktur, dan catatan keputusan arsitektur menjaga alasan di balik pilihan besar. Situs dokumentasi terbitan dibangun otomatis pada setiap penggabungan. Insinyur baru cepat produktif karena panduan orientasi dan runbook mutakhir dan dapat ditemukan, dan insinyur on-call bersandar pada runbook alih-alih memanggil penulis aslinya.

**Pemerintah.** Sebuah lembaga nasional mewarisi sistem dari kontraktor yang pergi, bergantung sepenuhnya pada dokumentasi untuk membawa pengetahuan melintasi batas kontrak. Karena vendor sebelumnya memelihara dokumentasi arsitektur, runbook, dan catatan keputusan sebagai keluaran wajib, tim baru dapat mengoperasikan dan memodifikasi sistem tanpa penulis aslinya. Di tempat dokumentasi tipis, lembaga menghadapi rekayasa balik yang mahal. Pengalaman itu mendorong kebijakan baru: dokumentasi adalah keluaran kontraktual, ditinjau untuk akurasi alih-alih diperlakukan sebagai renungan belakangan, dan runbook harus memungkinkan operator berwenang mana pun menanggapi insiden.

## Kasus bisnis: motivasi, ROI, dan TCO

Dokumentasi membayar Anda kembali dalam waktu orientasi yang lebih singkat, risiko orang kunci yang lebih rendah, respons insiden yang lebih cepat, dan biaya perubahan yang lebih rendah sepanjang umur sistem. Insinyur baru mencapai produktivitas dalam hari alih-alih minggu, staf on-call menyelesaikan insiden dari runbook alih-alih mengeskalasi, pemelihara mengubah sistem dengan percaya diri bertahun-tahun setelah dibangun: ini penghematan besar dan berulang yang berlipat di organisasi besar dan umur sistem yang panjang.

Berapa biaya dokumentasi? Upaya penulisan dan pemeliharaan. Berapa biaya *tidak* mendokumentasikan? Anda membayar terus-menerus: dalam orientasi lambat, pertanyaan berulang, hambatan orang kunci, pemulihan insiden lebih lambat, dan, di titik ekstrem, sistem yang tidak dapat diubah dengan aman oleh siapa pun, memaksa penulisan ulang mahal atau rekayasa balik. Dalam skenario transisi vendor dan audit, dokumentasi yang hilang dapat membawa biaya kontraktual dan kepatuhan langsung. Untuk meyakinkan pimpinan, beri angka pada waktu orientasi, waktu respons insiden, dan berapa banyak pengetahuan kritis yang berada di kepala individu. Lalu bingkai docs-as-code dan generasi sebagai cara mendapat dokumentasi tahan lama tanpa beban pemeliharaan yang setara. Dan tekankan bahwa dokumentasi yang tidak akurat adalah liabilitas, sehingga investasi harus mencakup menjaganya tetap mutakhir.

## Anti-pola dan jebakan

- **Dokumentasi basi disajikan sebagai mutakhir:** menyesatkan pembaca dan menghancurkan kepercayaan pada semua dokumentasi.
- **Wiki tulis-sekali:** halaman dibuat dan tidak pernah diperbarui, diam-diam menyimpang dari kenyataan.
- **Fragmentasi dokumentasi:** pengetahuan tersebar di banyak perkakas dan wiki sehingga tak ada yang dapat ditemukan.
- **Mencampur jenis dokumentasi:** tutorial, rujukan, dan penjelasan campur aduk dalam satu halaman, tidak melayani pembaca mana pun dengan baik.
- **Memelihara dengan tangan konten yang dapat dihasilkan:** dokumen API tulisan tangan yang pasti menyimpang dari antarmuka sebenarnya.
- **Pengetahuan suku:** pemahaman kritis yang hanya disimpan di kepala orang dan riwayat obrolan, hilang saat mereka pergi.
- **Dokumentasi sebagai renungan belakangan:** ditulis di akhir, jika sama sekali, alih-alih bersamaan dengan perubahan.
- **Tanpa kepemilikan:** dokumen tanpa pemilik yang bertanggung jawab membusuk karena memperbaruinya bukan tugas siapa pun.

## Model kematangan

- **Tingkat 1, Memulai.** Dokumentasi jarang, tersebar, dan basi, dan pengetahuan hidup di kepala orang. Apa yang ada ditulis sekali dan tidak pernah disentuh lagi, sehingga pemadaman atau kepergian berarti merekayasa balik sistem.
- **Tingkat 2, Mengembangkan.** Dokumen kunci ada, seperti README dan beberapa runbook, tetapi dipelihara tidak konsisten dan sulit ditemukan. Sebagian tim mendokumentasikan dengan baik dan yang lain nyaris tidak sama sekali, dan tidak ada ekspektasi bersama tentang apa yang harus dibawa repositori atau di mana ia harus berada.
- **Tingkat 3, Membakukan.** Docs-as-code adalah norma di seluruh organisasi: struktur umum seperti Diátaxis, rujukan API dan changelog hasil generate, catatan keputusan, dan ekspektasi dalam tinjauan bahwa dokumen berubah bersama kode yang dijelaskannya. Setiap dokumen bernilai tinggi punya pemilik bernama, dan ada satu rumah yang dikenal dengan pencarian nyata.
- **Tingkat 4, Mengelola.** Dokumentasi diukur, bukan sekadar ada. Anda melacak cakupan dokumen esensial, laju perubahan dokumen terhadap laju perubahan kode, waktu orientasi, penyelesaian insiden dari runbook saja, dan kesegaran terhadap ambang kebasian yang didefinisikan, dan meninjau metrik itu terhadap garis dasar. Pembusukan tertangkap secara mekanis lewat generasi, tes terhadap sistem, dan pemeriksaan tautan serta akurasi, dan halaman basi ditandai atau dipangkas berdasarkan bukti alih-alih kebetulan.
- **Tingkat 5, Mengorkestrasi.** Dokumentasi terus diperbaiki dan terintegrasi di seluruh organisasi: hidup, sebagian besar dihasilkan atau diuji terhadap sistem, dimiliki, dapat ditemukan, dan adaptif. Metrik memberi umpan balik ke tempat Anda berinvestasi, pengetahuan tersirat ditangkap sebagai bagian rutin pekerjaan, dan korpus diseimbangkan dan dipangkas secara aktif seiring berubahnya sistem, tim, dan pembaca.

## Gagasan untuk didiskusikan

- Dokumentasi mana, jika lenyap besok, yang paling menyakiti organisasi Anda, dan apakah sekarang ada serta tetap mutakhir?
- Bagaimana Anda menjadikan memperbarui dokumentasi bagian alami dari mengubah kode alih-alih tugas terpisah?
- Di mana Anda dapat mengganti dokumentasi tulisan tangan dengan dokumentasi hasil generate yang terikat pada sumber kebenaran?
- Bagaimana Anda mengukur apakah dokumentasi Anda akurat dan dipakai, bukan hanya ada?
- Bagaimana asisten AI harus mengubah cara Anda menulis, memelihara, dan mencari dokumentasi, dan di mana mereka mungkin memperkenalkan konten yang masuk akal tetapi keliru?
- Bagaimana Anda menangkap pengetahuan tersirat sebelum orang yang memegangnya pergi?

## Poin-poin utama

- Perlakukan dokumentasi sebagai kode: berversi, ditinjau, dekat dengan sumber, dan diterbitkan otomatis.
- Strukturkan konten menurut kebutuhan pembaca memakai tutorial, panduan cara-kerja, rujukan, dan penjelasan.
- Pelihara esensial bernilai tinggi: README, runbook, dokumen arsitektur, orientasi, dan catatan keputusan.
- Hasilkan dokumen API dan changelog agar tidak dapat menyimpang dari sumber kebenaran.
- Lawan pembusukan dengan kepemilikan, ekspektasi tinjauan, dan pemangkasan; dokumentasi yang tidak akurat lebih buruk daripada tidak ada.

## Referensi dan bacaan lanjutan

- Daniele Procida, kerangka dokumentasi *Diátaxis*
- Andrew Etter, *Modern Technical Writing*
- Anne Gentle, *Docs Like Code*
- Google, *Developer Documentation Style Guide* dan panduan Season of Docs (sebagai contoh rujukan)
- Michael Nygard, *Documenting Architecture Decisions* (catatan keputusan arsitektur)
- Andrew Hunt dan David Thomas, *The Pragmatic Programmer* (tentang pengetahuan dan dokumentasi)
- *Keep a Changelog* (sebagai konvensi rujukan)
