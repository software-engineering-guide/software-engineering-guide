# 2.6 Kontrol versi dan manajemen sumber

## Tinjauan dan motivasi

Anggap [kontrol versi](https://en.wikipedia.org/wiki/Version_control) sebagai sistem pencatat basis kode Anda. Ia menangkap setiap perubahan, termasuk siapa yang membuatnya, kapan, dan mengapa, dan memungkinkan banyak orang mengerjakan perangkat lunak yang sama tanpa saling menimpa. Bagi organisasi besar, ia jauh lebih dari sekadar cadangan. Ia adalah fondasi tempat kolaborasi, [integrasi berkelanjutan](https://en.wikipedia.org/wiki/Continuous_integration) (CI), audit, dan manajemen rilis bertumpu. Pilihan yang Anda buat tentang percabangan, struktur repositori, dan disiplin commit membentuk seberapa cepat tim Anda dapat bergerak, dan seberapa aman.

Bagi tim besar, manajemen sumber sesungguhnya adalah masalah koordinasi pada skala besar. Ketika ratusan insinyur mendorong perubahan ke kode bersama, mereka membutuhkan strategi yang menjaga penggabungan tetap kecil, menjaga jalur utama selalu dapat dirilis, dan menjaga riwayat tetap terbaca. Tim yang berintegrasi terus-menerus mengalir mulus. Tim yang membiarkan cabang menyimpang berminggu-minggu terhuyung dari satu krisis integrasi ke krisis berikutnya. Struktur repositori Anda, satu repo besar atau banyak, juga membentuk cara tim berbagi kode dan berkoordinasi.

Lingkungan enterprise dan pemerintah menambah beberapa tuntutan lagi: keterlacakan, kontrol akses, dan retensi. Sebuah perubahan mungkin perlu tertaut ke butir kerja yang disetujui untuk audit. Rahasia tidak boleh pernah masuk ke riwayat. Akses repositori harus menghormati batas keamanan. Di sini, praktik kontrol versi Anda menjadi bagian dari kerangka kendali organisasi, dan kesalahan seperti rahasia yang bocor atau riwayat yang tidak dapat diaudit dapat berakibat serius.

## Prinsip utama

- Integrasikan perubahan kecil dengan sering; divergensi panjang adalah akar kesulitan penggabungan.
- Jaga jalur utama selalu dapat dirilis.
- Riwayat adalah dokumentasi; tulis commit untuk pembaca masa depan yang harus memahami mengapa.
- Jangan pernah meng-commit rahasia; perlakukan rahasia apa pun yang mencapai riwayat sebagai telah dikompromikan.
- Otomatiskan penegakan kebersihan (hook, pemeriksaan CI) alih-alih mengandalkan disiplin saja.
- Pilih struktur repositori (mono vs poli) menurut bagaimana tim sebenarnya berbagi kode dan berkoordinasi, bukan mode.
- Tautkan perubahan ke alasannya (butir kerja, tiket, atau keputusan) untuk keterlacakan.

## Rekomendasi

### Pilih pengembangan berbasis trunk dengan cabang berumur pendek

Condonglah ke [pengembangan berbasis trunk](https://en.wikipedia.org/wiki/Trunk-based_development): integrasikan ke jalur utama bersama dengan sering, memakai cabang fitur berumur pendek yang diukur dalam jam atau hari, bukan minggu. Cabang pendek menjaga penggabungan tetap kecil dan integrasi berkelanjutan, dan kebiasaan itu sangat terkait dengan kinerja pengiriman yang tinggi. Ketika pekerjaan belum selesai, jangan parkir di cabang berumur panjang. Gunakan [feature flag](https://en.wikipedia.org/wiki/Feature_toggle), sakelar runtime yang menyembunyikan pekerjaan belum selesai, agar Anda dapat menggabungkannya dengan aman. Sisakan cabang rilis berumur panjang untuk dukungan multi-versi yang sejati, dan masuklah dengan mengetahui biaya pemeliharaan yang dikandungnya.

### Pilih model percabangan yang sesuai dengan irama rilis

Cocokkan [model percabangan](https://en.wikipedia.org/wiki/Branching_(version_control)) Anda dengan cara Anda sebenarnya merilis. Jika Anda men-deploy secara berkelanjutan, pengembangan berbasis trunk dengan percabangan minimal melayani Anda dengan baik. Jika Anda merilis versi bernomor kepada pelanggan, atau mendukung beberapa versi hidup sekaligus, Anda mungkin memerlukan cabang rilis dan back-porting. Jauhi model berat dengan banyak cabang berumur panjang kecuali model rilis Anda benar-benar menuntutnya, karena itu melipatgandakan beban penggabungan dan pemeliharaan.

### Putuskan monorepo vs polirepo dengan sengaja

Raihlah [monorepo](https://en.wikipedia.org/wiki/Monorepo), satu repositori yang memegang banyak proyek, ketika tim banyak berbagi kode, memerlukan perubahan lintas proyek yang atomik, dan menginginkan perkakas serta visibilitas yang terpadu. Sebagai imbalannya, Anda menerima kebutuhan akan perkakas build dan kontrol akses yang berskala. Raihlah polirepo, repositori terpisah per proyek atau layanan, ketika tim dan layanan benar-benar independen, menginginkan akses dan siklus rilis yang terisolasi, dan tidak memerlukan perubahan lintas repo yang atomik. Sebagai imbalannya, Anda menerima biaya mengoordinasikan perubahan yang melintasi repositori. Keduanya berfungsi pada skala besar. Pilihan yang salah untuk pola kopling Anda yang menciptakan gesekan konstan.

### Tegakkan kebersihan commit dan commit konvensional

Mintalah pesan commit yang menjelaskan mengapa perubahan dibuat, bukan hanya apa. Adopsi konvensi seperti commit konvensional agar pesan terstruktur dan dapat diurai mesin, yang memungkinkan Anda mengotomatiskan changelog dan pembuatan versi. Jaga commit atomik, satu perubahan logis masing-masing, agar riwayat tetap dapat di-bisect dan mudah dibatalkan. Biarkan hook dan pemeriksaan CI menegakkan format pesan dan kebersihan dasar, alih-alih mengandalkan ingatan.

### Jauhkan biner besar dan kode hasil generate dari riwayat biasa

Jangan meng-commit aset biner besar langsung ke riwayat utama, karena membengkakkan setiap clone selamanya. Gunakan mekanisme penyimpanan berkas besar atau repositori artefak sebagai gantinya. Sebagai aturan, hindari juga meng-commit kode hasil generate; hasilkan di build. Ketika Anda benar-benar harus meng-commit artefak hasil generate, isolasi dan tandai dengan jelas agar tidak mencemari tinjauan dan diff.

### Cegah rahasia masuk ke repositori sama sekali

Letakkan pemindaian rahasia otomatis di pre-commit hook dan CI agar kredensial diblokir sebelum pernah mendarat. Berikan insinyur sistem manajemen rahasia yang layak, agar mereka tidak pernah perlu meng-hardcode kredensial sejak awal. Dan perlakukan rahasia apa pun yang mencapai riwayat sebagai telah dikompromikan: rotasi segera. Begitu rahasia di-push dan di-clone, menghapusnya dari riwayat sulit dan tidak andal.

### Tetapkan kontrol akses dan keterlacakan

Atur akses repositori agar menghormati batas keamanan dan [hak istimewa minimum](https://en.wikipedia.org/wiki/Principle_of_least_privilege). Tautkan commit atau pull request ke butir kerja, agar setiap perubahan dapat dilacak ke alasannya, yang membantu konteks rekayasa sehari-hari maupun audit. Lindungi cabang kunci Anda dengan pemeriksaan dan tinjauan yang diwajibkan, agar tidak ada yang digabung tanpa melewati gerbang yang telah Anda sepakati.

## Trade-off: kelebihan dan kekurangan

| Pilihan | Kelebihan | Kekurangan |
|---|---|---|
| Pengembangan berbasis trunk | Integrasi berkelanjutan; penggabungan kecil; aliran tinggi | Memerlukan feature flag dan disiplin; isolasi lebih sedikit |
| Cabang fitur berumur panjang | Isolasi kuat atas pekerjaan dalam proses | Penggabungan menyakitkan; integrasi tertunda; penyimpangan |
| Monorepo | Perubahan lintas proyek atomik; perkakas bersama; visibilitas | Perlu perkakas build berskala; kontrol akses kasar secara bawaan |
| Polirepo | Rilis independen; akses terisolasi; perkakas per repo sederhana | Perubahan lintas repo sulit; beban koordinasi versi |
| Commit konvensional | Changelog dan pembuatan versi otomatis; riwayat konsisten | Konvensi di muka; perlu penegakan |

Trade-off besarnya di sini adalah frekuensi integrasi versus isolasi. Cabang berumur panjang terasa lebih aman karena pekerjaan Anda berada sendirian, tetapi isolasi itulah yang menyebabkan penggabungan mahal dan kejutan integrasi di kemudian hari. Pengembangan berbasis trunk melepaskan perasaan isolasi itu demi integrasi berkelanjutan yang murah, dan meminta Anda membawa feature flag dan disiplin. Keputusan monorepo/polirepo menukar kemudahan lintas proyek dengan independensi tim. Pilih yang cocok dengan seberapa erat kode Anda sebenarnya berpasangan.

## Pertanyaan untuk didiskusikan dengan tim Anda

1. **Pemeriksaan apa yang harus lolos sebelum apa pun digabung ke jalur utama terlindung Anda, dan apakah jalur utama itu benar-benar selalu dapat dirilis?** Bab ini memperlakukan jalur utama yang dapat dirilis sebagai prinsip inti dan menyebut jalur utama tak terlindung, di mana kode rusak atau belum ditinjau mencapai cabang yang diandalkan semua orang, sebagai anti-pola. Pada tim besar jalur utama merah memblokir semua orang sekaligus, jadi gerbang yang Anda wajibkan adalah sifat keselamatan bersama, bukan pribadi. Bawa buktinya: apa yang sebenarnya ditegakkan perlindungan cabang Anda hari ini, dan seberapa sering jalur utama saat ini rusak. Putuskan rangkaian yang diwajibkan, tes lolos, pemindaian keamanan, dan tinjauan, dan jadikan jalur utama dapat dirilis berdasarkan kebijakan alih-alih harapan. Gerbang itulah yang memungkinkan banyak orang berintegrasi terus-menerus tanpa takut.

2. **Apakah mengadopsi commit konvensional sepadan dengan beban konvensinya bagi tim Anda, mengingat apa yang diotomatiskannya?** Bab ini merekomendasikan pesan commit terstruktur dan dapat diurai mesin justru karena memungkinkan Anda mengotomatiskan changelog dan pembuatan versi, dan meminta commit atomik agar riwayat tetap dapat di-bisect dan dibatalkan. Trade-off-nya nyata: Anda membayar konvensi di muka dan membutuhkan penegakan, sebagai imbalan catatan rilis yang dihasilkan dan riwayat yang andal. Bawa sinyal apa yang Anda lakukan secara manual hari ini, seperti menulis changelog dengan tangan atau berburu commit mana yang memperkenalkan regresi. Jika Anda sering merilis atau memelihara beberapa versi, otomasi biasanya balik modal; jika Anda jarang memotong rilis, konvensi yang lebih ringan mungkin cukup. Biarkan hook dan CI menegakkan format agar tidak bergantung pada ingatan.

3. **Apakah Anda telah menerima biaya operasional yang dituntut struktur repositori Anda, entah perkakas monorepo atau koordinasi lintas repo?** Bab ini mengatakan baik monorepo maupun polirepo berfungsi pada skala besar, dan bahwa pilihan yang salah untuk pola kopling Anda yang menciptakan gesekan konstan. Monorepo membutuhkan perkakas build berskala dan kontrol akses yang lebih halus, sementara polirepo menjadikan perubahan apa pun yang melintasi repositori sebagai proyek koordinasi dengan risiko ketidaksejajaran versi. Bawa sinyal konkret: seberapa sering perubahan Anda melintasi batas proyek, dan apakah perkakas build serta akses Anda dapat memikul struktur yang Anda miliki. Jika perubahan atomik lintas proyek umum, berinvestasilah pada perkakas monorepo; jika tim dan layanan benar-benar independen, terima biaya koordinasi lintas repo dengan sengaja. Intinya adalah mencocokkan struktur dengan seberapa erat kode Anda sebenarnya berpasangan, lalu mendanai perkakas yang dibutuhkan struktur itu.

4. **Jika kredensial hidup di-commit ke repositori yang sibuk sekarang juga, seberapa cepat Anda akan mendeteksinya, dan apakah rotasi benar-benar otomatis, bukan harapan?** Bab ini memperlakukan rahasia apa pun yang mencapai riwayat sebagai telah dikompromikan dan memperingatkan bahwa menghapusnya kemudian sulit dan tidak andal, sehingga pencegahan dan rotasi cepat adalah satu-satunya pertahanan nyata. Bagi tim besar paparan itu berlipat: rahasia yang di-push ke repo bersama di-clone ke puluhan mesin dan dicerminkan ke cache CI dalam hitungan menit, sehingga respons manusia yang lambat menjamin pelanggaran. Pertimbangan yang bersaing adalah gesekan: pemindaian pre-commit yang agresif dan rotasi paksa memperlambat orang dan menghasilkan positif palsu, jadi Anda harus menyetel kontrol alih-alih mematikannya. Bawa buktinya: apakah pemindaian rahasia berjalan di pre-commit hook maupun CI, waktu rata-rata Anda untuk mendeteksi dan merotasi kebocoran yang diketahui, dan apakah insinyur bahkan punya sistem manajemen rahasia yang menghilangkan godaan untuk meng-hardcode. Dalam konteks enterprise dan pemerintah, kaitkan ini dengan proses insiden dan aturan retensi Anda, karena kredensial bocor dalam riwayat yang dapat diaudit adalah peristiwa keamanan sekaligus kepatuhan, dan regulator akan menanyakan siapa yang tahu dan seberapa cepat mereka bertindak.

5. **Apakah cabang Anda benar-benar berumur pendek, dan di mana tidak, mengapa pekerjaan belum selesai diparkir di cabang alih-alih disembunyikan di balik feature flag?** Bab ini condong keras ke pengembangan berbasis trunk karena divergensi panjang adalah akar kesulitan penggabungan, dan menawarkan feature flag sebagai mekanisme yang memungkinkan Anda menggabungkan pekerjaan tak lengkap dengan aman alih-alih mengisolasinya berminggu-minggu. Pada tim besar ini sifat koordinasi, bukan preferensi pribadi: setiap cabang yang hidup berminggu-minggu menjadi fork pribadi dari kenyataan yang harus direkonsiliasi seseorang, dan biaya rekonsiliasi itu tumbuh seiring jumlah personel. Pertimbangan yang bersaing adalah bahwa feature flag membawa biayanya sendiri, termasuk kompleksitas runtime, menguji kombinasi, dan flag basi yang harus dipensiunkan. Bawa datanya: distribusi umur cabang Anda yang sebenarnya, seberapa sering integrasi menghasilkan konflik atau kejutan, dan berapa banyak cabang berumur panjang yang ada sekarang dan mengapa. Untuk organisasi besar atau yang diatur, tambahkan gambaran rilis, karena dukungan multi-versi yang sejati dapat membenarkan cabang rilis berumur panjang dengan back-porting yang disiplin, dan itu keputusan berbeda dari memarkir kerja fitur sehari-hari di luar jalur utama.

6. **Dapatkah setiap perubahan dalam riwayat Anda dilacak ke penulis dan alasannya dalam batas keamanan yang tepat, dan akankah itu bertahan dari audit?** Bab ini memperlakukan kontrol akses, hak istimewa minimum, dan menautkan perubahan ke butir kerja sebagai bagian dari kerangka kendali organisasi, bukan polesan opsional. Bagi tim besar, keterlacakan adalah yang mengubah aliran commit yang buram menjadi sesuatu yang dapat Anda nalar selama insiden atau tinjauan kepatuhan, dan batas akses adalah yang mencegah satu akun yang dikompromikan menjangkau kode yang tidak semestinya ia sentuh. Pertimbangan yang bersaing adalah kecepatan pengembang: tautan butir kerja wajib, izin berbutir halus, dan tinjauan yang diwajibkan menambah upacara yang mungkin wajar dilewati tim kecil yang bergerak cepat. Bawa buktinya: apakah cabang terlindung benar-benar mensyaratkan pemeriksaan dan tinjauan yang Anda klaim, apakah commit benar-benar merujuk butir kerja yang disetujui, dan bagaimana akses dipetakan ke batas keamanan Anda yang sebenarnya hari ini. Dalam konteks enterprise dan pemerintah, kaitkan ini dengan klasifikasi, retensi, dan kewajiban audit, karena riwayat yang tidak dapat diaudit atau pemberian akses yang terlalu luas menjadi temuan yang dapat menghentikan program atau menggagalkan akreditasi.

## Lensa sektor

**Startup.** Kecepatan dan kelangsungan hidup menang. Gunakan satu repositori, bekerja berbasis trunk, gabungkan cabang berumur pendek beberapa kali sehari, dan sembunyikan pekerjaan belum selesai di balik feature flag sederhana alih-alih cabang panjang. Nyalakan pemindaian rahasia sejak commit pertama, karena kunci bocor di repo publik dapat menenggelamkan perusahaan tanpa tim keamanan untuk menahannya. Lewati model percabangan rumit dan proses berat; cabang main yang terlindung dan pesan commit yang bermakna sudah cukup disiplin untuk bergerak cepat.

**Bisnis kecil.** Tanpa spesialis platform atau DevOps khusus dan dengan anggaran ketat, belilah bawaan terkelola alih-alih membangunnya. Penyedia Git yang di-hosting memberi Anda perlindungan cabang, tinjauan yang diwajibkan, dan pemindaian rahasia siap pakai, jadi bersandarlah pada itu alih-alih meng-host server sendiri yang tidak dapat Anda pelihara. Bingkai keputusan sebagai kebersihan data: ketahui repositori mana yang memegang konfigurasi sensitif, simpan kredensial di pengelola rahasia penyedia, dan biarkan platform menegakkan beberapa aturan yang benar-benar Anda butuhkan.

**Enterprise.** Masalah yang sulit adalah konsistensi di banyak tim. Bakukan perlindungan cabang, konvensi commit, dan pemindaian rahasia sebagai kebijakan seluruh organisasi agar kelompok berhenti menciptakan ulang, dan buat pilihan monorepo-versus-polirepo dengan sengaja per pola kopling, mendanai perkakas build berskala atau koordinasi lintas repo yang dituntutnya. Rutekan perubahan ke peninjau yang tepat dengan aturan kepemilikan kode, tautkan commit ke butir kerja untuk keterlacakan, dan perlakukan kebersihan kontrol versi sebagai kontrol yang diatur dengan pemilik dan metrik, bukan soal kebiasaan individu.

**Pemerintah.** Aturan pengadaan, transparansi, dan akuntabilitas publik membentuk seluruh pengaturan. Wajibkan setiap commit merujuk butir kerja yang disetujui, kendalikan akses per batas klasifikasi, dan jadikan pemindaian rahasia serta rotasi segera wajib di bawah proses insiden terdokumentasi. Dukung beberapa versi yang di-deploy dengan cabang rilis berumur panjang dan back-porting yang disiplin di tempat situs tidak dapat semuanya meningkatkan versi sekaligus, dan jaga riwayat tetap dapat diaudit dan tersimpan agar permintaan akreditasi, keterbukaan informasi, dan pengawasan dapat dijawab tanpa kelabakan.

## Contoh

**Startup.** Sebuah startup tiga orang bekerja berbasis trunk karena kebiasaan dan keharusan, menggabungkan cabang berumur pendek ke main beberapa kali sehari dan menyembunyikan fitur setengah jadi di balik flag sederhana. Mereka menyalakan pemindaian rahasia di CI sejak commit pertama, karena kunci API bocor di repo publik dapat menenggelamkan perusahaan yang tidak punya tim keamanan untuk menahan dampaknya. Satu repositori, cabang main terlindung, dan pesan commit bermakna memberi mereka disiplin yang cukup untuk bergerak cepat tanpa tersandung riwayat mereka sendiri.

**Enterprise.** Sebuah perusahaan teknologi besar menjalankan monorepo dengan ratusan layanan dan pustaka bersama. Perkakas build berskala dan aturan kepemilikan kode merutekan setiap perubahan ke peninjau yang tepat. Satu commit dapat memperbarui pustaka bersama dan setiap konsumennya secara atomik sekaligus, menghindari masalah ketidaksejajaran versi yang menghantui repositori terdistribusi. Pengembangan berbasis trunk dengan feature flag menjaga jalur utama dapat dirilis, dan pemindaian rahasia memblokir kredensial pada saat commit di seluruh repositori.

**Pemerintah.** Seorang kontraktor pertahanan nasional berpegang pada keterlacakan yang ketat. Setiap commit harus merujuk butir kerja yang disetujui. Perlindungan cabang mensyaratkan pemindaian keamanan yang lolos dan tinjauan independen, dan akses dikendalikan ketat per batas klasifikasi. Pemindaian rahasia wajib, dan kredensial yang terekspos memicu rotasi segera di bawah proses insiden. Cabang rilis berumur panjang mendukung beberapa versi yang di-deploy di situs yang tidak dapat semuanya meningkatkan versi sekaligus, dengan back-porting perbaikan keamanan yang disiplin.

## Kasus bisnis: motivasi, ROI, dan TCO

Manajemen sumber yang baik nyaris gratis untuk diadopsi dan mahal bila ditiadakan. Pengembangan berbasis trunk dan integrasi berkelanjutan termasuk praktik yang paling kuat terkait dengan kinerja pengiriman perangkat lunak yang tinggi, yang pada gilirannya berkorelasi dengan hasil organisasi yang lebih baik. Riwayat yang bersih dan dapat dilacak memangkas waktu mendiagnosis insiden dan memenuhi audit, dan percabangan yang disiplin menyelamatkan Anda dari biaya berulang yang tidak dianggarkan berupa krisis integrasi dan maraton penggabungan.

Risiko timpang terbesar adalah rahasia dalam kontrol versi. Satu kredensial bocor dapat menyebabkan pelanggaran yang biayanya melampaui investasi perkakas mana pun, dan riwayat membuat kebocoran semacam itu bertahan. Mencegahnya murah; membersihkan sesudahnya tidak. Pilihan struktur yang buruk tampak sebagai gesekan kronis: setiap perubahan lintas repo menjadi proyek koordinasi, atau setiap build monorepo menjadi hambatan. Untuk meyakinkan pimpinan, kaitkan strategi percabangan Anda dengan metrik pengiriman dan waktu diagnosis insiden, dan bingkai pemindaian rahasia serta kontrol akses sebagai kontrol berbiaya rendah terhadap risiko pelanggaran dan audit berbiaya tinggi.

## Anti-pola dan jebakan

- **Cabang menyimpang berumur panjang:** berminggu-minggu kerja terisolasi yang digabung menjadi peristiwa integrasi yang menyakitkan dan berisiko.
- **Rahasia dalam riwayat:** kredensial yang di-hardcode yang bertahan di clone selamanya dan memerlukan rotasi begitu terekspos.
- **Meng-commit biner besar ke riwayat utama:** membengkakkan setiap clone secara permanen dan memperlambat semua operasi.
- **Pesan commit tak bermakna:** "fix", "wip", "changes" yang menghancurkan nilai riwayat sebagai dokumentasi.
- **Meng-commit kode hasil generate seolah ditulis tangan:** diff berisik, konflik penggabungan, dan kebingungan tentang sumber kebenaran.
- **Struktur repo yang salah untuk kopling:** polirepo untuk kode yang berpasangan erat, atau monorepo tanpa perkakas berskala.
- **Jalur utama tak terlindung:** tanpa pemeriksaan wajib, sehingga kode rusak atau belum ditinjau mencapai cabang yang diandalkan semua orang.

## Model kematangan

- **Tingkat 1, Memulai:** Ad hoc dan reaktif. Percabangan diimprovisasi, cabang hidup berminggu-minggu, pesan commit berbunyi "fix" atau "wip", tidak ada pemindaian rahasia, dan integrasi terhuyung dari satu krisis penggabungan ke krisis berikutnya.
- **Tingkat 2, Mengembangkan:** Praktik dasar muncul tetapi bervariasi menurut tim. Model percabangan dan konvensi pesan ada di beberapa tempat, namun cabang masih hidup terlalu lama, penegakan parsial, pemindaian rahasia tambal-sulam, dan struktur repo diwarisi alih-alih dipilih.
- **Tingkat 3, Membakukan:** Praktik didokumentasikan dan ditegakkan di seluruh organisasi: pengembangan berbasis trunk dengan cabang pendek, jalur utama terlindung yang selalu dapat dirilis, konvensi commit yang ditegakkan, pemindaian rahasia di hook maupun CI, akses hak istimewa minimum, dan pilihan monorepo atau polirepo yang disengaja.
- **Tingkat 4, Mengelola:** Praktik sumber diukur dan dikendalikan dengan data. Anda melacak umur cabang, frekuensi integrasi, tingkat jalur utama rusak, waktu rata-rata mendeteksi dan merotasi rahasia bocor, serta keterlacakan perubahan-ke-butir-kerja terhadap garis dasar yang disepakati, dan Anda bertindak ketika angkanya menyimpang alih-alih menunggu insiden berikutnya.
- **Tingkat 5, Mengorkestrasi:** Praktik terus diperbaiki dan terintegrasi di seluruh organisasi. Percabangan, struktur repo, dan perkakas beradaptasi seiring tim dan kopling kode berubah, otomasi menegakkan kebersihan dari ujung ke ujung, dan data kontrol versi memberi makan keputusan pengiriman, keamanan, dan risiko di seluruh organisasi.

## Gagasan untuk didiskusikan

- Apakah umur cabang tim Anda benar-benar pendek, dan jika tidak, apa yang mencegah integrasi berkelanjutan?
- Apakah pilihan monorepo atau polirepo Anda cocok dengan seberapa erat kode Anda sebenarnya berpasangan?
- Bagaimana Anda menangani biner besar dan artefak hasil generate hari ini, dan berapa biayanya bagi Anda?
- Apa yang akan terjadi jika kredensial hidup di-commit sekarang, dan seberapa cepat Anda akan mendeteksi dan merotasinya?
- Berapa banyak disiplin pesan commit dan keterlacakan yang layak ditegakkan untuk konteks Anda?
- Bagaimana feature flag mengubah strategi percabangan Anda, dan risiko baru apa yang dibawanya?

## Poin-poin utama

- Integrasikan dengan sering memakai cabang berumur pendek; divergensi panjang menyebabkan kesulitan yang tampaknya dihindarinya.
- Jaga jalur utama dapat dirilis dan terlindung oleh pemeriksaan yang diwajibkan.
- Jangan pernah biarkan rahasia masuk ke riwayat; pindai otomatis dan rotasi segera jika masuk.
- Pilih monorepo atau polirepo menurut kebutuhan kopling dan koordinasi Anda yang sebenarnya.
- Perlakukan riwayat commit sebagai dokumentasi, dengan commit yang bermakna, konvensional, dan atomik.

## Referensi dan bacaan lanjutan

- Nicole Forsgren, Jez Humble, Gene Kim, *Accelerate: The Science of Lean Software and DevOps*
- Jez Humble dan David Farley, *Continuous Delivery*
- Scott Chacon dan Ben Straub, *Pro Git*
- Paul Hammant dan lainnya, tulisan tentang pengembangan berbasis trunk
- Spesifikasi Conventional Commits (sebagai standar rujukan)
- Martin Fowler, artikel tentang pola percabangan dan integrasi berkelanjutan
